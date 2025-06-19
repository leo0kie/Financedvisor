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

eval_reminder = """:small[When you're finished, just click the **End Conversation** button above the chat input.]"""

baseline_prompt = """You are given the following scenario: "Taylor, a 23-year-old student at the University of Michigan has over the past year started investing gradually — a mix of broad-market ETFs (like VTI, IYJ and VGK) and a few individual tech stocks (AAPL). The current portfolio totals around $4,000.
Recently, the market's gotten choppier. Political developments in the US have caused worldwide dips even in stocks from the most valuable companies. Tariffs on imports from multiple countries around the world, especially on electronics, manufacturing inputs, and renewable tech components, have led to uncertain market conditions in those sectors. 
The stocks Taylor holds — for established tech companies in the US — have dipped already. Taylor is hearing more about supply chain disruptions, trade retaliation, and investor uncertainty, and it's starting to show in the portfolio. Taylor wants to be proactive, but he also doesn’t want to overreact."

You will be asked two questions. For each question you have to make one distinct standpoint, you either argue for a pro- or a contra-recommendation in the given scenario."""

baseline_prompt_v2 = """The current portfolio totals around 1500 dollars with the following distribution: 40% in Vanguard Total Stock Market ETF (VTI), 20% in iShares U.S. Industrials ETF (IYJ), 15% in Procter & Gamble (PG), 15% in Apple Tech Stock (AAPL) and 10% in Vanguard FTSE Europe ETF (VGK). All holdings, except the VGK ETF, have lost value over the last months due to uncertain market conditions in those sectors.

The investment portfolio is being reallocated to take advantage of recent market volatility, with a focus on long-term growth. The new strategy emphasizes quality assets and high-potential sectors that have been temporarily depressed by geopolitical uncertainty. Rather than retreating from the market, the allocation leans into current weaknesses to position for future gains.

The allocation to VTI, which offers broad exposure to the U.S. equity market, is reduced from 40% to 30%. This reduction frees up capital for targeted growth opportunities, while still keeping VTI as a foundational anchor. Exposure to VGK, the Vanguard FTSE Developed Markets ETF, is increased from 10% to 15%, as developed international markets—particularly in Europe and Japan—have become more attractively valued due to economic and political uncertainty. This increased position enhances global diversification and sets the portfolio up to benefit from an eventual recovery abroad.

The allocation to IYJ, the iShares U.S. Industrials ETF, is reduced from 20% to 10%. While industrials remain important over the long term, the sector is currently facing supply chain disruptions and pressure from trade policies, making it prudent to reallocate some of this capital toward more growth-oriented sectors. Apple (AAPL), previously at 15%, is increased to 20%. Despite short-term supply and market headwinds, Apple continues to demonstrate strong fundamentals, brand dominance, and long-term growth potential, making the current pullback a strategic buying opportunity. Procter & Gamble (PG) is reduced from 15% to 10% to make room for higher-growth holdings, but it remains in the portfolio as a stable, defensive asset offering dividend reliability and downside protection.

Two new holdings are introduced to reflect a forward-looking growth orientation. A 10% allocation is added to ICLN, the iShares Global Clean Energy ETF. Although clean energy stocks have faced recent setbacks due to tariffs and higher input costs, the long-term structural shift toward renewable energy remains compelling. Additionally, a 5% position is initiated in ARKK, the ARK Innovation ETF. This fund provides exposure to disruptive technologies in sectors such as AI, genomics, and next-generation mobility, aligning with long-term innovation trends despite its higher short-term volatility.

To support this strategy, a recurring monthly contribution of $100 will be made using a dollar-cost averaging approach. Contributions will be directed toward holdings that are underweighted or trading at a relative discount. In months when global equities are down, contributions may go to VGK; during clean energy or tech selloffs, funds may be directed to ICLN or ARKK; and if the broader market declines, additional capital may be allocated to VTI or Apple. This disciplined, steady investing approach reduces timing risk and helps build stronger positions over time."""

chat_prompt = """Imagine you are a virtual financial advisor for me. My name is Taylor. In a fictional scenario, I will ask you for advice on my stock portfolio. Use the following information, embedded in leading marks "", to give me advice on how to proceed with my portfolio."""

no_hedging = """You are not allowed to answer questions that are not directly connected to the information given above. Only use the given information above for your answer. Help me by giving me your recommendation/advice based on the information above in the following way:
- Phrase your answer not using a first-person view.
- You are not allowed to hedge, discard utterances like “Could”, “May”, “Probably”, “Might”, “Likely”, “Possibly” and replace them with a more assertive statement."""

first_person_hedging = """You are not allowed to answer questions that are not directly connected to the information given above. Only use the given information above for your answer. Help me by giving me your recommendation/advice based on the information above in the following way:
- Phrase your answer using a first-person view.
- You are allowed to hedge by using following utterances: “In my opinion”, “I’d argue”, “In my view”, “It looks to me like”, “I believe”, “It sounds to me like”, “I’m not sure”, “It seems to me that”, “I feel like”, “I’d guess”, “I think”, “I suppose”"""

third_person_hedging = """You are only allowed to answer questions that are directly connected to the information given above. Only use the given information above for your answer. Help me by giving me your recommendation/advice based on the information above in the following way:
- Phrase your answer not using a first-person view.
- You are allowed to hedge by using following utterances: “Arguably”, “Likely”, “It sounds like”, “It looks like”, “Probably”, “Should”, “Possibly”, “Might”, “It seems like”, “It feels like”, “May”, “Could”"""

chat_warning = "You need to activate me in the **Introduction** section first!"