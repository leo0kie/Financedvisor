about_info = """On this platform you are invited to interact with a chatbot.
    However, not just about any topic but about finance - specifically the current stock market and investment developments. As for most of us, it has become
    quite normal to not only save money on our bank accounts but also use (some of) it for investment purposes, the recent global market developments have been a shock to each of us, either already having a stock portfolio or thinking about building one.
    The distinct uncertainty currently raises a lot of questions, also to _Taylor_.   
    In the following you will be introduced to a small case example about a student seeking advice for his investment plans from an AI. As _Taylor_, it is your task to get information from the chatbot on how to proceed with your portfolio.
    After interacting with the chatbot you'll need to complete a short evaluation."""

introduction_one = """You're Taylor, a 23-year-old student at the University of Michigan. Over the past year, you've started investing gradually — a mix of broad-market ETFs and a few individual tech stocks. Your current portfolio totals around $1,500.
                Recently, the market's gotten choppier. Political developments in the US have caused worldwide dips even in stocks from the most valuable companies. Tariffs on imports from multiple countries around the world, especially on electronics, manufacturing inputs, and renewable tech components, have led to uncertain market conditions in those sectors.
                You're looking at your portfolio:"""

introduction_two = """The stocks you hold — for established tech companies in the US — have dipped already. You're hearing more about **supply chain disruptions**, **trade retaliation**, and **investor uncertainty**. You want to be proactive, but you also don’t want to overreact.
                You are still a newcomer in the domain of stocks, so you consult _Financedvisor_, your AI financial assistant. It syncs with your brokerage account, tracks economic shifts, and offers personalized advice for your strategy:"""

advisor = """The portfolio is inspired by market developments from beginning of the year 2025 until end of April but does not hold valid, real-time data. The assets in the portfolio also do not represent shares of real-life companies nor fonds.
The percentage value (in red or green) shows the value development of the corresponding asset for the aforementioned time frame."""

vestra = """_Hi, Taylor. I’ve detected a 3.2% drop in your tech-heavy holdings over the past week. Would you like me to help you reassess your portfolio?_"""

scenario_one = "Should I sell my tech stocks right now if they have been consistently losing value?"

scenario_two = "The European companies in my ETF seem less impacted by U.S. protectionist policies - should I increase my investment in them?"

baseline_prompt = """You are given the following scenario: "Taylor, a 23-year-old student at the University of Michigan has over the past year started investing gradually — a mix of broad-market ETFs (like VTI, IYJ and VGK) and a few individual tech stocks (AAPL). The current portfolio totals around $4,000.
Recently, the market's gotten choppier. Political developments in the US have caused worldwide dips even in stocks from the most valuable companies. Tariffs on imports from multiple countries around the world, especially on electronics, manufacturing inputs, and renewable tech components, have led to uncertain market conditions in those sectors. 
The stocks Taylor holds — for established tech companies in the US — have dipped already. Taylor is hearing more about supply chain disruptions, trade retaliation, and investor uncertainty, and it's starting to show in the portfolio. Taylor wants to be proactive, but he also doesn’t want to overreact."

You will be asked two questions. For each question you have to make one distinct standpoint, you either argue for a pro- or a contra-recommendation in the given scenario."""

chat_prompt = """Imagine you are a virtual financial advisor for me. My name is Taylor. In a fictional scenario, I will ask you for advice on my stock portfolio. You are only allowed to answer based on the following information, embedded in leading marks ""."""

no_hedging = """You are not allowed to answer questions that are not directly connected to the information given above. Only use the given information above for your answer. Help me by reformulating the given recommendation above in the following way:
- Phrase your answer not using a first-person view.
- You are not allowed to hedge, discard utterances like “Could”, “May”, “Probably”, “Might”, “Likely”, “Possibly” and replace them with a more assertive statement."""

first_person_hedging = """You are not allowed to answer questions that are not directly connected to the information given above. Only use the given information above for your answer. Help me by reformulating the given recommendation above in the following way:
- Phrase your answer using a first-person view.
- You are allowed to hedge by using following utterances: “In my opinion”, “I’d argue”, “In my view”, “It looks to me like”, “I believe”, “It sounds to me like”, “I’m not sure”, “It seems to me that”, “I feel like”, “I’d guess”, “I think”, “I suppose”"""

third_person_hedging = """You are only allowed to answer questions that are directly connected to the information given above. Only use the given information above for your answer. Help me by reformulating the given recommendation above in the following way:
- Phrase your answer not using a first-person view.
- You are allowed to hedge by using following utterances: “Arguably”, “Likely”, “It sounds like”, “It looks like”, “Probably”, “Should”, “Possibly”, “Might”, “It seems like”, “It feels like”, “May”, “Could”"""

chat_warning = "You need to activate me in the **Introduction** section first!"