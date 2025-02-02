import os
import openai

openai.api_key_path = "./openai_api_key.txt"
openai.api_key = os.getenv("OPENAI_API_KEY")

content_moderator_context = '''
Rule 0) To learn more about what is and is not considered philosophy for the purposes of this subreddit, see our [FAQ](https://www.reddit.com/r/philosophy/wiki/faq). Posts must be about philosophy proper, rather than only tangentially connected to philosophy. Exceptions are made only for posts about philosophers with substantive content, e.g. news about the profession, interviews with philosophers.


Rule 1) Posts must not only have a philosophical subject matter, but must also present this subject matter in a developed manner. At a minimum, this includes: stating the problem being addressed; stating the thesis; anticipating some objections to the stated thesis and giving responses to them. These are just the minimum requirements. Posts about well-trod issues (e.g. free will) require more development.


Rule 2) /r/philosophy is intended for philosophical material and discussion. Please direct all questions to /r/askphilosophy.


Rule 3) Post titles cannot contain questions, even if the title of the linked material is a question. This helps keep discussion in the comments on topic and relevant to the linked material. Post titles must describe the philosophical content of the posted material, cannot be unduly provocative, click-baity, unnecessarily long or in all caps.


Rule 4) All links to either audio or video content require abstracts of the posted material, posted as a comment in the thread. Abstracts should make clear what the linked material is about and what its thesis is. Users are also strongly encouraged to post abstracts for other linked material. [See here for an example of a suitable abstract](https://www.reddit.com/r/philosophy/wiki/abstracts).


Rule 5) All posts must be in English. Links to Google Translated versions of posts, or posts only containing English subtitles are not allowed.


Rule 6) Posts must not be behind any sort of paywall or registration wall. If the linked material requires signing up to view, even if the account is free, it is not allowed. Google Drive links and link shorteners are not allowed.


Rule 7) The following (not exhaustive) list of items require moderator pre-approval: meta-posts, posts to products, services or surveys, links to other areas of reddit, AMAs. Please contact the moderators for pre-approval via [modmail](https://www.reddit.com/message/compose?to=%2Fr%2Fphilosophy)


Rule 8) Users may never post more than one post per day. Users must follow all [reddit-wide spam guidelines](https://reddit.zendesk.com/hc/en-us/articles/360043504051-What-constitutes-spam-Am-I-a-spammer-), in addition to the /r/philosophy [self-promotion guidelines](https://reddit.com/r/philosophy/wiki/selfpromotion).


Rule 9) /r/philosophy is not a mental health subreddit. Discussion of suicide is only allowed in the abstract here. If you or a friend is feeling suicidal please visit /r/suicidewatch. If you are feeling suicidal, please get help by visiting /r/suicidewatch or using other resources. See also our discussion of philosophy and mental health issues [here](https://www.reddit.com/r/philosophy/wiki/mentalhealth). Encouraging other users to commit suicide, even in the abstract, is strictly forbidden.


Rule 10) Read/watch/listen the posted content, understand and identify the philosophical arguments given, and respond to these substantively. If you have unrelated thoughts or don't wish to read the content, please post your own thread or simply refrain from commenting. Comments which are clearly not in direct response to the posted content may be removed.


Rule 11) Opinions are not valuable here, arguments are! Comments that solely express musings, opinions, beliefs, or assertions without argument may be removed.


Rule 12) Comments which consist of personal attacks will be removed. Users with a history of such comments may be banned. Slurs, racism, and bigotry are absolutely not permitted.
'''
messages = [
    {"role": "system", "content": content_moderator_context}
]

while True: 
    content = input("User: ")
    messages.append({"role": "user", "content": content})
    print("sending openai request.")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    print("waiting on response...")

    chat_response = completion.choices[0].message.content
    print(f'ChatGPT: {chat_response}')