from telegram import Bot
import random
import time
import asyncio
import logging
from telegram.error import InvalidToken


# Logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


# Liste mit Bot-Tokens von @BotFather
BOT_TOKENS = [
    '7800580139:AAELacZwDJG_Zs6vixHEqib49F15VwFYYPQ', 
    '7624739257:AAH9HmXUKUI1JG6TYKc11rtkolW-hLmk3uE', 
    '7455531156:AAGH2koy0ctCJq3C6MyvLrnKdc74frXIARs', 
    '7813758444:AAFKn5GrJVBbQl6sTwJpCVH4eGKgg_2CZh0', 
    '7785362982:AAFIAjug9ozhZL2oQpbihWnm_g7vO4LnxUE', 
     
]

# Telegram-Gruppen-ID, in der die Bots Nachrichten senden sollen
GROUP_ID = -1002344430008  # Gruppen-ID (z. B. -123456789) Minus muss vor der Nummer sein! 

# Liste mit zufälligen Nachrichten
MESSAGES = [
    "Kirby is going to the moon! 🚀",
    "Who's holding KIRBY for the long term? 💎🙌",
    "What a great community we have here!",
    "Just bought more KIRBY! Feeling bullish! 🐂",
    "Any predictions for KIRBY's price next week?",
    "KIRBY is my favorite crypto project!",
    "Don't miss this gem, it's going places! 🌟",
    "Can someone share the latest KIRBY news?",
    "I believe in KIRBY's potential. Strong fundamentals! 💪",
    "Who's ready for KIRBY to hit new all-time highs? 🚀",
    "The KIRBY roadmap looks impressive. 🚀",
    "HODLing strong! Never selling my KIRBY! 💎",
    "How did you discover KIRBY? Let’s share our stories!",
    "KIRBY partnerships are so exciting. 🔗",
    "This dip is a blessing. Time to accumulate more!",
    "The KIRBY team is doing an amazing job!",
    "What do you guys think of the recent market trends?",
    "Kirby Army! Let’s spread the word! 🌍",
    "The community support for KIRBY is unreal!",
    "KIRBY will change the crypto game forever! 🔥",
    "I’m so glad I joined this project early!",
    "If you’re not in KIRBY yet, what are you waiting for?",
    "Who else is super excited for the next big update?",
    "Big whales are accumulating KIRBY, don’t sleep on it!",
    "Let’s build the strongest community in crypto! 💥",
    "This is the start of something HUGE for KIRBY!",
    "Don’t FOMO in later; now’s the time to get in! ⏳",
    "KIRBY is trending on social media, let’s keep it up!",
    "Massive respect to everyone who’s been here since day one!",
    "What’s your target price for KIRBY by the end of the year?",
    "KIRBY memes are 🔥. Let’s create and share more!",
    "I’m holding KIRBY for the long term. Big things coming!",
    "Who else thinks KIRBY will dominate the crypto space?",
    "Great vibes in this group! Love the Kirby Army! ❤️",
    "KIRBY utility is what sets it apart from other projects!",
    "Get ready for KIRBY to break resistance levels!",
    "The liquidity on KIRBY pairs looks strong!",
    "Always do your own research, but KIRBY is a no-brainer!",
    "Imagine where KIRBY will be in 5 years. 🌟",
    "Community-driven projects like KIRBY are the future!",
    "What exchanges would you like to see KIRBY listed on next?",
    "This is just the beginning for KIRBY. The sky’s the limit!",
    "Who else believes KIRBY will be the next big thing in crypto? 🚀",
    "The devs are on fire! KIRBY just keeps getting better! 🔥",
    "KIRBY to $1? Why not dream big! 💭",
    "I can’t wait for the next big announcement from the team!",
    "Let’s invite more people to this amazing community! 📈",
    "Every dip is an opportunity! Buy the dip, HODL the moon! 🚀",
    "KIRBY’s volume is skyrocketing. Are you paying attention?",
    "We’re all early adopters of something revolutionary! 🥳",
    "This is the strongest community in crypto, no doubt!",
    "Imagine when KIRBY is featured in the top crypto news sites!",
    "Don’t sleep on KIRBY; it’s a hidden gem! 💎",
    "What’s the next milestone for KIRBY? Let’s discuss!",
    "The way KIRBY is trending, mass adoption is just around the corner!",
    "KIRBY memes are unmatched! Keep them coming! 😂",
    "What’s your KIRBY investment strategy? Share your tips!",
    "The tokenomics of KIRBY are just perfect. Long-term hold for sure!",
    "The community here feels like a family. Kirby Army! ❤️",
    "Big players are noticing KIRBY. The whales are coming!",
    "I can’t stop telling my friends about KIRBY!",
    "How’s everyone feeling about the market today?",
    "Another day, another step closer to KIRBY’s success! 🌟",
    "KIRBY could easily be the next big crypto influencer’s favorite!",
    "What’s your go-to source for KIRBY news and updates?",
    "With KIRBY, I feel like I’m part of something groundbreaking!",
    "Every day I hold KIRBY, I feel more confident in my decision. 💎",
    "Who’s ready for KIRBY to break all-time highs? 🚀",
    "The liquidity on KIRBY is looking stronger every day!",
    "I’ve been researching KIRBY for weeks, and it just keeps impressing me!",
    "Let’s make KIRBY go viral on Twitter today! Who’s in? 🐦",
    "I love how transparent and hardworking the KIRBY team is!",
    "This is the best crypto community I’ve ever been a part of!",
    "I’m holding KIRBY not just for gains but because I believe in the vision!",
    "Let’s share our KIRBY success stories to motivate others!",
    "Kirby Army is unstoppable. The hype is real! 🔥",
    "What’s the best meme you’ve seen about KIRBY this week?",
    "KIRBY’s roadmap is so detailed. I can’t wait to see it all unfold!",
    "Imagine when big investors finally realize KIRBY’s potential!",
    "Who’s here for the long term? KIRBY is a marathon, not a sprint!",
    "Does anyone else check KIRBY’s price like 10 times a day? 😂",
    "If you love KIRBY, make sure to spread the word! 📣",
    "Crypto projects like KIRBY restore my faith in this space.",
    "Let’s plan a KIRBY meetup one day! That would be epic!",
    "The more I learn about KIRBY, the more I want to invest!",
   "Who else feels like KIRBY is the next big thing? 🚀",
   "Every HODLer deserves a pat on the back! 💎🙌",
   "What’s your favorite KIRBY feature so far?",
   "The roadmap is incredible. KIRBY is going places!",
   "Imagine KIRBY hitting a new ATH. It’s coming! 🚀",
   "Whales are silently accumulating KIRBY. Are you ready?",
   "The energy in this community is unmatched! ❤️",
   "Remember, buy the dip and enjoy the ride! 🐂",
   "When KIRBY hits $1, what’s your first move?",
   "This is just the beginning for KIRBY holders. 🌟",
   "Spread the word. KIRBY Army is taking over! 🌍",
   "What do you love most about KIRBY’s vision?",
   "We’re building something revolutionary here!",
   "Have you checked out the latest KIRBY updates?",
   "KIRBY memes are taking over the crypto world!",
   "Which exchanges do you want to see KIRBY on next?",
   "I’m so proud to be part of this project! 🚀",
   "This community is what sets KIRBY apart.",
   "The team is working tirelessly for us. Kudos to them!",
   "Every day is a good day to HODL KIRBY! 💎",
   "Mass adoption is closer than we think. Get ready!",
   "Are you sharing KIRBY with your friends? Let’s grow!",
   "KIRBY’s utility is unmatched in the crypto space.",
   "Who’s excited for the next big KIRBY milestone?",
   "Every dip is a blessing in disguise. Accumulate more!",
   "Imagine the possibilities once KIRBY goes viral!",
   "This is one of the strongest communities in crypto.",
   "The hype is real. KIRBY is here to stay! 🔥",
   "Which country should host the first KIRBY meetup?",
   "What’s your price prediction for KIRBY this year?",
   "The KIRBY team deserves all the praise! 👏",
   "Crypto history is being made with KIRBY!",
   "Keep calm and HODL KIRBY. 🚀",
   "Who else checks the KIRBY price every hour? 😂",
   "Get ready for the next big announcement. It’s coming!",
   "What’s the best KIRBY meme you’ve seen recently?",
   "Big things happen when great communities come together!",
   "KIRBY’s growth is unstoppable. Just watch!",
   "Which feature are you most excited about in KIRBY?",
   "Crypto Twitter is buzzing about KIRBY right now! 🐦",
   "This project has more potential than anything I’ve seen!",
   "Don’t sleep on KIRBY. The future is bright! 🌟",
   "What’s your favorite thing about the KIRBY community?",
   "It feels amazing to be early in a project like this.",
   "KIRBY will set a new standard in the crypto space.",
   "The liquidity on KIRBY pairs is looking great!",
   "Every milestone we hit proves the power of this community.",
   "What’s your favorite crypto besides KIRBY? 👀",
   "Imagine KIRBY as the top 10 token. It’s possible!",
   "The tokenomics of KIRBY are simply brilliant.",
   "The journey to success is better together. Go KIRBY!",
   "Crypto markets are volatile, but KIRBY is steady. 💪",
   "What do you think of KIRBY’s marketing campaigns?",
   "Imagine the partnerships KIRBY will land next!",
   "Where do you see KIRBY in five years? 🚀",
   "This is the most welcoming crypto group ever!",
   "What’s your biggest crypto success story so far?",
   "KIRBY’s transparency sets it apart from the rest.",
   "How many KIRBY tokens are you holding? 💎",
   "Let’s make KIRBY trend again on Twitter today!",
   "What’s your favorite KIRBY update so far?",
   "Who’s been here since day one? OG KIRBY fans!",
   "Crypto adoption is happening fast. KIRBY leads the way!",
   "What’s the best time to buy more KIRBY? Always!",
   "Who else believes KIRBY is a hidden gem? 💎",
   "KIRBY partnerships will surprise everyone soon!",
   "What’s the next big feature you’d like to see in KIRBY?",
   "Have you invited your friends to join KIRBY Army yet?",
   "Crypto isn’t just money. It’s a revolution! 🚀",
   "The KIRBY roadmap looks so promising!",
   "Let’s keep this community active and growing!",
   "KIRBY memes are better than coffee in the morning! ☕",
   "What are your long-term plans for holding KIRBY?",
   "The team behind KIRBY deserves more recognition!",
   "Who else feels like we’re building the future here?",
   "Crypto whales are taking notice of KIRBY!",
   "What’s the next big crypto trend you see coming?",
   "This is more than a token. It’s a family.",
   "Crypto isn’t a bubble. It’s just getting started!",
   "Imagine the next exchange listing for KIRBY. 🚀",
   "What’s your favorite feature of the staking platform?",
   "This community makes me proud every single day!",
   "KIRBY is proof that good projects succeed!",
   "We’re all part of something revolutionary here!",
   "What’s the best advice you’d give to new HODLers?",
   "Stay patient and trust the process. Go KIRBY!",
   "What do you think sets KIRBY apart from competitors?",
   "What’s your go-to strategy during a market dip? 🐻➡️🐂",
   "Who’s got diamond hands here? 💎🙌",
   "What’s your dream crypto portfolio look like? 📊",
   "Crypto is the future. Are you ready for it? 🌍🚀",
   "What was your first crypto investment? Let’s hear the stories! 📈",
   "How did you discover KIRBY? Share your journey! 🛤️",
   "What do you think about KIRBY’s tokenomics? Brilliant, right? 📖",
   "Crypto adoption is happening faster than anyone predicted! 🌍💡",
   "What’s the best lesson you’ve learned in crypto so far? 🧠",
   "When do you think we’ll see a global crypto boom? 🌐",
   "Who else feels like they’re part of something historic with KIRBY? 🏛️",
   "What’s your favorite KIRBY feature? Let’s talk utility! 🔧",
   "Crypto memes are 🔥. Let’s create some KIRBY-themed ones!",
   "The KIRBY roadmap is so well planned. What’s your favorite milestone? 🗺️",
   "KIRBY to $1? Let’s dream big and make it happen! 💭🚀",
   "Who else checks crypto prices first thing in the morning? 😂📱",
   "The world is waking up to crypto. Are you ahead of the curve? 🌐💎",
   "Let’s talk partnerships. What’s your dream collaboration for KIRBY? 🤝",
   "Crypto isn’t a gamble; it’s a calculated risk. 📊💡",
   "What’s the most exciting trend in crypto right now? 🚀",
   "KIRBY’s liquidity pool is growing steadily. That’s bullish! 🐂",
   "Who else is bullish on KIRBY’s future? 🐂🔥",
   "Crypto can be volatile, but HODLers always win in the end! 💎🙌",
   "When moon? When Lambo? 🚀😂",
   "Crypto is a rollercoaster, but we’re all here for the ride! 🎢",
   "Who else loves watching blockchain explorers? Or just me? 👀",
   "Crypto whales are noticing KIRBY. Big things are coming! 🐋💰",
   "KIRBY is proof that community-driven projects can succeed! ❤️",
   "Who’s ready for KIRBY’s next big milestone? 🚀",
   "If KIRBY could partner with any company, which one would you pick? 🤝",
   "Let’s dream big: KIRBY as a top 10 crypto by market cap! 💎📈",
   "Who else feels like KIRBY is a hidden gem? 💎🔥",
   "What’s the one thing you love most about crypto? 🌍",
   "Imagine a future where KIRBY powers real-world applications! 🔧",
   "Every HODLer deserves a medal for their patience. 🏅",
   "Crypto isn’t a trend; it’s a revolution. 🚀",
   "What’s the most underrated crypto project you’ve seen (besides KIRBY)? 🤔",
   "What do you think the next big innovation in blockchain will be? 🧠",
   "Crypto history is being written right now. Glad we’re part of it! 🏛️",
   "How many people have you introduced to KIRBY so far? Let’s grow together! 🌱",
   "The more I learn about crypto, the more bullish I become. 📖🔥",
   "Imagine if every business accepted crypto tomorrow. The future is near! 🛒",
   "What’s your top tip for staying calm during market dips? 🧘‍♂️",
   "The crypto community is the best part of the industry! ❤️",
   "Who else checks their wallet balance like it’s a scoreboard? 😂",
   "Imagine a world where crypto is the default currency. 🌍",
   "What’s the best crypto advice you’ve ever received? 💡",
   "Who else feels like crypto changed their life for the better? 🌟",
   "What’s your ultimate crypto goal? Financial freedom? 🌴💰",
   "How do you explain crypto to your non-crypto friends? 🤔",
   "Crypto is the future, and we’re here early! 🕰️🚀",
   "What’s your favorite thing about DeFi? 🌐📊",
   "Crypto memes make the bear markets bearable! 😂",
   "Every dip is just a chance to stack more. 💎📈",
   "What’s the most exciting feature of the KIRBY ecosystem for you? 🌟",
   "Crypto feels like magic when it clicks. 🔮✨",
   "Let’s make KIRBY trend on Twitter today! Who’s in? 🐦🔥",
   "What’s your prediction for crypto adoption in the next 5 years? 🌍",
   "Who else loves the transparency of blockchain technology? 🔍",
   "Crypto isn’t just a fad; it’s a paradigm shift! 🌍🚀",
   "What’s your favorite crypto success story so far? 🌟",
   "Crypto education is key. What’s the best resource you’ve found? 📚",
   "Imagine paying for coffee with KIRBY. The future is near! ☕💰",
   "KIRBY’s community feels like family. ❤️",
   "What’s the best way to onboard someone into crypto? 🛤️",
   "Crypto markets may be volatile, but our faith in KIRBY isn’t! 🔥",
   "What’s the most exciting crypto event you’ve ever attended? 🎉",
   "Imagine KIRBY-powered apps in everyday life. The possibilities are endless! 🔧",
   "What’s the most surprising thing you’ve learned about blockchain? 🤔",
   "Every day in crypto feels like a new adventure! 🌍",
   "What’s your favorite thing about the KIRBY roadmap? 🗺️",
   "Who else loves the long-term vision of the KIRBY team? 🔮",
   "Imagine a world where KIRBY is the backbone of DeFi. 🌐",
   "Crypto bridges the gap between dreams and reality. 🌟",
   "Every new crypto milestone feels like history in the making! 🏛️",
   "What’s your favorite crypto project outside of KIRBY? 🤔",
   "What’s the most fun part of being in the crypto space? 🎉",
   "Who else feels like they’re part of a revolution with KIRBY? ❤️",
   "What’s your go-to tool for tracking crypto prices? 📱",
   "The power of blockchain is just beginning to be unleashed! 🔗",
   "Crypto rewards the patient. Stay strong, HODLers! 💎",
   "What’s the one thing you’d tell a new crypto investor? 🧠",
   "Imagine a future where KIRBY is a household name. 🏠🚀",
   "What’s the best thing about the crypto community? ❤️",
   "Every day we build, we’re one step closer to changing the world! 🌍",
   "What’s your biggest lesson learned from crypto trading? 🧠",
   "If KIRBY were a superhero, what would its powers be? 🦸‍♂️",
   "Imagine a crypto-themed video game. What would it be like? 🎮",
   "Crypto makes Mondays bearable. Who agrees? 😎",
   "What’s the funniest thing you’ve seen in a crypto chat? 😂",
   "Describe your crypto journey in 3 words. Go! 🚀",
   "Who else feels like they’re in a sci-fi movie with blockchain tech? 🤖",
   "What’s your dream blockchain application? 🛠️",
   "What’s the most creative crypto merch you’ve ever seen? 👕",
   "If KIRBY were a drink, what would it taste like? 🍹",
   "Imagine explaining blockchain to a 5-year-old. How would you do it? 🤔",
   "What’s the coolest crypto sticker you own? 🚀",
   "How do you celebrate crypto milestones? 🥳",
   "What’s your go-to crypto research tool? 📊",
   "Crypto memes are the lifeblood of the community. What’s your favorite? 😂",
   "Who else thinks blockchain tech could revolutionize voting? 🗳️",
   "Crypto slang 101: What’s your favorite term? 🚀",
   "What’s the most futuristic thing about crypto? 🔮",
   "Describe the crypto market with a movie title. 🎬",
   "Crypto is like a rollercoaster, but what’s the view at the top? 🎢",
   "What’s the weirdest use case for blockchain you’ve heard of? 🤯",
   "If you could invent a new crypto token, what would it be called? 💡",
   "What’s the best crypto advice you’d give to a beginner? 🌱",
   "What’s the most random thing you’ve bought with crypto? 🛒",
   "Imagine paying rent with KIRBY. The future is now! 🏠",
   "Who else loves checking blockchain explorers just for fun? 👀",
   "Crypto mining: Art, science, or madness? ⛏️",
   "What’s your favorite crypto documentary or YouTube channel? 🎥",
   "Describe the feeling of buying your first crypto in one word. 🥳",
   "What’s the best crypto app you can’t live without? 📱",
   "Imagine a crypto-themed TV show. What would it be called? 📺",
   "What’s the best blockchain use case you’ve seen so far? 🔗",
   "If you could meet one blockchain developer, who would it be? 👨‍💻",
   "Crypto FOMO is real, but how do you deal with it? ⏳",
   "What’s the weirdest thing someone has said about crypto to you? 🧐",
   "Imagine a KIRBY mascot. What would it look like? 🐾",
   "What’s the most innovative crypto feature you’ve used? 🚀",
   "Crypto education is the key to adoption. What’s your favorite resource? 📚",
   "Describe the crypto space in one emoji. 🤔",
   "What’s your dream crypto portfolio size? 💰",
   "If KIRBY had a mascot, what would its name be? 🐾",
   "Who else thinks crypto-themed board games would be awesome? 🎲",
   "What’s your favorite crypto quote? 💬",
   "How has crypto changed your view on finance? 🌍",
   "What’s your favorite blockchain explorer? 🔍",
   "Imagine your pet could trade crypto. Would they HODL or panic sell? 🐾😂",
   "What’s the best crypto event you’ve attended (or wish you could)? 🎉",
   "If KIRBY were a spaceship, where would it travel first? 🚀",
   "Crypto staking feels like growing a financial garden. 🌱",
   "Describe KIRBY’s potential in one sentence. 💎",
   "What’s your favorite crypto Easter egg in apps or games? 🐣",
   "Crypto whitepapers: Fascinating or boring? 📄",
   "What’s the most exciting blockchain innovation right now? 🔮",
   "Imagine KIRBY in a sci-fi novel. What’s the plot? 📖",
   "What’s your dream partnership for KIRBY? 🤝",
   "Describe KIRBY’s vision in 3 words. 🌟",
   "What’s the most surprising thing you’ve learned about crypto? 🤔",
   "Crypto is freedom. Agree or disagree? 🌍",
   "What’s the coolest feature of your favorite crypto wallet? 💼",
   "Imagine the blockchain as a person. What would they be like? 🤖",
   "What’s your favorite crypto conference moment? 🎤",
   "Crypto or fiat: Which one feels more natural to you now? 💸",
   "Describe your HODLing strategy in one meme. 😂",
   "Crypto staking: Passive income or active commitment? 💰",
   "What’s the weirdest blockchain project you’ve seen? 🧐",
   "Imagine a KIRBY comic book. What would the story be? 📚",
   "What’s your favorite crypto reward program? 🎁",
   "What do you think will be the next big crypto breakthrough? 🔧",
   "Describe your first crypto trade in one emoji. 🤯",
   "What’s your favorite crypto use case beyond finance? 🌐",
   "Crypto regulations: Good, bad, or necessary? ⚖️",
   "Imagine a crypto-themed amusement park. What’s the main ride? 🎢",
   "What’s your favorite blockchain success story? 🌟",
   "What do you think is the next big crypto trend? 🚀",
   "Crypto adoption is happening. What’s your prediction for 2030? 🔮",
   "Describe KIRBY in 3 emojis. 🚀💎🔥",
   "Crypto burns through misconceptions. What’s the biggest myth you’ve debunked? 🔥", 
   "What’s your go-to crypto research strategy? 📊",
   "What’s your favorite crypto analogy? 📖",
   "What’s the most exciting thing about DeFi for you? 🌐",
   "Imagine a crypto-themed RPG. What’s the main quest? ⚔️",
   "What’s your favorite thing about KIRBY’s ecosystem? 💎",
   "If KIRBY were a movie, what genre would it be? 🎥",
   "Describe your favorite crypto day in one word. 🥳",
   "What’s the best thing about blockchain for artists? 🎨",
   "Imagine a crypto museum. What’s the centerpiece? 🏛️",
   "What’s the coolest thing you’ve ever bought with crypto? 🛒",
   "If you could change one thing about crypto, what would it be? 🌟",
   "Describe blockchain technology to someone who’s never heard of it. 🧠",
   "Crypto staking feels like playing the long game. Who’s with me? 💎",
   "What’s your go-to way to explain crypto to beginners? 🗣️",
   "What’s your favorite part of the KIRBY community? ❤️",
   "Imagine the perfect crypto city. What’s it like? 🌆",
   "What’s the best part about HODLing? 💪",
   "What’s your favorite crypto trivia fact? 📖",
   "Crypto is evolving fast. Where do you see it in 5 years? 🔮",
   "What’s the most exciting part of being in the crypto space right now? 🌍",

]

# Bild-URLs (öffentlich zugänglich)
IMAGE_URLS = [
    "https://framerusercontent.com/images/qfATvfbda3L3GAJB8iBrqrDho.png?scale-down-to=512",
    "https://framerusercontent.com/images/8xmOXup7zQEUU3TBmLldNJKf368.png?scale-down-to=512",
    "https://pbs.twimg.com/media/Ge3l9_jW4AESTIR?format=jpg&name=large",
    "https://framerusercontent.com/images/jueCwRu3VJBi747RozdlWUYfA.png?scale-down-to=512",
    "https://framerusercontent.com/images/gb1lNvakebdA52HrU6mDjhJ9cEg.png?scale-down-to=1024",
    "https://framerusercontent.com/images/6vXP4kI3u7P1ZjqqzDXvf9QZFuA.jpeg?scale-down-to=1024",
    

    
]
# Social Links
SOCIAL_LINKS = [
    "https://x.com/Kirbyonkas_",
    "https://www.kirbyonkas.com/",
    "https://dapp.chainge.finance/?fromChain=KAS&toChain=KAS&fromToken=USDT&toToken=KIRBY",
    "https://kas.fyi/token/krc20/KIRBY",
    "https://www.biconomy.com/exchange/KIRBY_USDT",
    "https://www.kaspiano.com/token/kirby?ref=kirby",
]

# Zufällige Nachricht auswählen
def get_random_message():
    return random.choice(MESSAGES)

# Zufälliges Bild auswählen
def get_random_image():
    return random.choice(IMAGE_URLS)

# Zufälligen Social-Link auswählen
def get_random_social_link():
    return random.choice(SOCIAL_LINKS)

# Asynchrone Funktion zum Senden von Nachrichten, Bildern und Links
async def bot_send_messages(bot_token):
    bot = Bot(token=bot_token)
    while True:
        try:
            # Zufällige Entscheidung: Nachricht, Bild oder Social Link senden
            choice = random.choices(
                ["message", "image", "link"], weights=[0.7, 0.1, 0.2], k=1
            )[0]

            if choice == "message":
                message = get_random_message()
                await bot.send_message(chat_id=GROUP_ID, text=message)
                logging.info(f"Bot {bot_token} sent message: {message}")
            elif choice == "image":
                image_url = get_random_image()
                await bot.send_photo(chat_id=GROUP_ID, photo=image_url)
                logging.info(f"Bot {bot_token} sent image: {image_url}")
            elif choice == "link":
                social_link = get_random_social_link()
                await bot.send_message(chat_id=GROUP_ID, text=social_link)
                logging.info(f"Bot {bot_token} posted social link: {social_link}")
            
            # Pause
            await asyncio.sleep(random.randint(600, 6000)) # Pause zwischen Aktionen
        except Exception as e:
            logging.error(f"Error with Bot {bot_token}: {e}")
            await asyncio.sleep(30)  # Bei Fehlern 30 Sekunden warten

# Hauptfunktion zum Starten aller Bots
async def main():
    tasks = [bot_send_messages(token) for token in BOT_TOKENS]
    await asyncio.gather(*tasks)

# Programm starten
if __name__ == "__main__":
    asyncio.run(main())