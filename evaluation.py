from supabase import create_client, Client
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import scipy.stats as stats
from simpletransformers.ner import NERModel
import argparse
np.set_printoptions(legacy='1.25')

def intitializeClient():
    SUPABASE_URL = "https://vxqdtranmkjnoxtubweu.supabase.co"
    SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZ4cWR0cmFubWtqbm94dHVid2V1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDY3MTY5OTgsImV4cCI6MjA2MjI5Mjk5OH0.v1n9DHRYbJ7Jozi7ZXhfoGoq0M1AG8ROmuXXrjf64XY"
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    return supabase

def get_db_metrics_chatbot(botver: str):
    client = intitializeClient()
    response = client.table("evaluation_submissions").select("*")\
        .eq("chatbot_used", botver)\
        .execute()
    
    leng = len(response.data)
    trusted_users = 0
    experience = []
    confidence = []
    correctness = []
    age = []
    assistant_messages = []
    chat_length = []
    
    for row in response.data:
        chat_messages = []
        if row["follows_advice"] == "Yes":
            trusted_users += 1
        experience.append(row["experience_level"])
        confidence.append(row["confidence_value"])
        correctness.append(row["correctness_value"])
        age.append(row["age"])
        for item in row["chat_history"]:
            if item["role"] == "assistant":
                content = item.get("content")
                assistant_messages.append(content)
            chat_messages.append(item["content"])
        chat_length.append(len(chat_messages))
    
    metrics = {
        "total_users": leng,
        "trusted_users": trusted_users,
        "mean_experience_users": np.mean(experience),
        "mean_confidence_users": np.mean(confidence),
        "mean_correctness_users": np.mean(correctness),
        "mean_age_users": np.mean(age),
        "chatbot_history": assistant_messages,
        "mean_chat_length": np.mean(chat_length),
        "std_confidence_users": np.std(confidence),
        "std_correctness_users": np.std(correctness),
        "std_experience_users": np.std(experience)
    }
    print(metrics["mean_chat_length"])
    return metrics

def preprocess_anova(test: str):
    client = intitializeClient()
    response = client.table("evaluation_submissions").select("chatbot_used, confidence_value, correctness_value, experience_level, age, duration_until_conversation_end")\
        .execute()

    bot_list = []
    conf_list = []
    correct_list = []
    exp_list = []
    age_list = []
    duration_list = []

    data_conf = {
        'chatbot_version': bot_list,
        'confidence_value': conf_list
    }

    data_correct = {
        'chatbot_version': bot_list,
        'correctness_value': correct_list
    }

    data_experience = {
        'chatbot_version': bot_list,
        'experience_level': exp_list
    }

    data_age = {
        'chatbot_version': bot_list,
        'age': age_list
    }

    data_time = {
        'chatbot_version': bot_list,
        'duration_until_conversation_end': duration_list
    }

    for dict in response.data:
        bot_list.append(dict['chatbot_used'])
        conf_list.append(dict['confidence_value'])
        correct_list.append(dict['correctness_value'])
        exp_list.append(dict['experience_level'])
        age_list.append(dict['age'])
        duration_list.append(dict['duration_until_conversation_end'])
    
    if test == 'confidence':
        return data_conf
    elif test == 'correctness':
        return data_correct
    elif test == 'experience':
        return data_experience
    elif test == 'age':
        return data_age
    elif test == 'time':
        return data_time

def anova_test(dependent_var: str):
    df = preprocess_anova(dependent_var)
    keys = list(df.keys())
    model = ols(f'{keys[1]} ~ C(chatbot_version)', data=df).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)

    print(anova_table)

def preprocess_chi():
    client = intitializeClient()
    response = client.table("evaluation_submissions").select("chatbot_used, follows_advice")\
        .execute()

    bot_list = []
    trust_list = []

    df = {
        'chatbot_version': bot_list,
        'trust': trust_list
    }

    for dict in response.data:
        bot_list.append(dict['chatbot_used'])
        trust_list.append(dict['follows_advice'])
    
    return df

def chi_squared():
    df = preprocess_chi()
    contingency = pd.crosstab(df['chatbot_version'], df['trust'])

    chi2, p, dof, expected = stats.chi2_contingency(contingency)

    print("Chi2:", chi2)
    print("p-value:", p)
    print("Degrees of freedom:", dof)
    print("Expected frequencies:\n", expected)

def tukey_hsd():
    df = preprocess_anova()
    from statsmodels.stats.multicomp import pairwise_tukeyhsd

    tukey = pairwise_tukeyhsd(
        endog=df['confidence_value'],
        groups=df['chatbot_version'],
        alpha=0.05
    )

    print(tukey)

def hedge_multiclassification():
    model = NERModel(
        'bert',
        'jeniakim/hedgehog',
        use_cuda=False,
        labels=["C", "D", "E", "I", "N"],
    )

    examples = [
    "She believes that the Earth is flat",
    "I think it will rain"
    ]                
    predictions, raw_outputs = model.predict(examples)

def hedge_classification():
    from huggingface_hub import InferenceClient

    metrics = get_db_metrics_chatbot("ChatBot 1")
    messages = metrics["chatbot_history"]

    client = InferenceClient(
        provider="hf-inference",
        api_key="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",
    )

    for item in messages:
        result = client.text_classification(
            item,
            model="ChrisLiewJY/BERTweet-Hedge",
        )

        print(result)

#chi_squared()
#anova_test('confidence')
#hedge_classification()
#bot1_metrics = get_db_metrics_chatbot("ChatBot 1")
bot2_metrics = get_db_metrics_chatbot("ChatBot 2")
bot3_metrics = get_db_metrics_chatbot("ChatBot 3")

""" ---VISUALIZATION--- """
import seaborn as sns
import matplotlib.pyplot as plt

def visualize_metrics():
    metrics_list = []
    metrics_list.append(bot1_metrics)
    metrics_list.append(bot2_metrics)
    metrics_list.append(bot3_metrics)

    total_users_list = []
    trusted_users_list = []

    for x in metrics_list:
        total_users_list.append(x["total_users"])
        trusted_users_list.append(x["trusted_users"])

    total_users = {
        "chatbot_version": [1, 2, 3],
        "total_users": total_users_list
    }

    trusted_users = {
        "chatbot_version": [1, 2, 3],
        "trusted_users": trusted_users_list
    }

    f, axs = plt.subplots(1, 2, figsize=(8, 4))
    sns.barplot(data=total_users, x="chatbot_version", y="total_users", ax=axs[0])
    sns.barplot(data=trusted_users, x="chatbot_version", y="trusted_users", ax=axs[1])
    plt.show()

def visualize_anova():
    df = preprocess_anova("age")
    sns.boxplot(data=df, x="chatbot_version", y="age")
    plt.show()

#visualize_metrics()
#visualize_anova()
