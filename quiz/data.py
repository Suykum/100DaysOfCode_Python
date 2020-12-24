import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 17,
    "difficulty": "medium"
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
# question_data = [
#     {
#         "category": "Science: Computers",
#         "type": "boolean", "difficulty": "medium",
#         "question": "The HTML5 standard was published in 2014.",
#         "correct_answer": "True",
#         "incorrect_answers": ["False"]
#     },
#     {
#         "category": "Science: Computers", "type": "boolean", "difficulty": "medium",
#         "question": "The common software-programming acronym &quot;I18N&quot; "
#                     "comes from the term &quot;Interlocalization&quot;.",
#         "correct_answer": "False", "incorrect_answers": ["True"]
#     },
#     {
#         "category": "Science: Computers", "type": "boolean", "difficulty": "medium",
#         "question": "FLAC stands for &quot;Free Lossless Audio Condenser&quot;&#039;", "correct_answer": "False",
#         "incorrect_answers": ["True"]
#     },
#     {
#         "category": "Science: Computers", "type": "boolean", "difficulty": "medium",
#         "question": "The open source program Redis is a relational database server.",
#         "correct_answer": "False", "incorrect_answers": ["True"]
#     },
#     {
#         "category": "Science: Computers", "type": "boolean", "difficulty": "medium",
#         "question": "Early RAM was directly seated onto the motherboard and could not be easily removed.",
#         "correct_answer": "True", "incorrect_answers": ["False"]
#     },
#     {
#         "category": "Science: Computers", "type": "boolean", "difficulty": "medium",
#         "question": "The first dual-core CPU was the Intel Pentium D.", "correct_answer": "False",
#         "incorrect_answers": ["True"]
#     },
#     {
#         "category": "Science: Computers", "type": "boolean", "difficulty": "medium",
#         "question": "The last Windows operating system to be based on the Windows 9x kernel was Windows 98.",
#         "correct_answer": "False", "incorrect_answers": ["True"]
#     },
#     {
#         "category": "Science: Computers", "type": "boolean", "difficulty": "medium",
#         "question": "Android versions are named in alphabetical order.", "correct_answer": "True",
#         "incorrect_answers": ["False"]
#     },
#     {
#         "category": "Science: Computers", "type": "boolean", "difficulty": "medium",
#         "question": "Linus Sebastian is the creator of the Linux kernel, which went on to be used in Linux,"
#                     " Android, and Chrome OS.",
#         "correct_answer": "False", "incorrect_answers": ["True"]
#     },
#     {
#         "category": "Science: Computers", "type": "boolean", "difficulty": "medium",
#         "question": "A Boolean value of &quot;0&quot; represents which of these words?", "correct_answer": "False",
#         "incorrect_answers": ["True"]}
# ]
