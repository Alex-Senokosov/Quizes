# 1.
# data = [
#     {
#         "question": 'Сколько будет 2 + 3 ?',
#         "answers": [
#             {
#                 "id": '1',
#                 "value": '4',
#                 "isCorrect": False
#             }
#         ]
#     }
# ]
# print(data[0]['question'])


# 2.
# def renderQuestion(index):
#     print('123: ' + str(index))
# renderQuestion(67)
#
# renderQuestion2 = lambda index: print('123: ' + str(index))
# renderQuestion2(67)

# 3.
# data = [
#     {
#         "question": 'Сколько будет 2 + 3 ?',
#         "answers": [
#             {
#                 "id": '1',
#                 "value": '4',
#                 "isCorrect": False
#             },
#             {
#                 "id": '2',
#                 "value": '5',
#                 "isCorrect": False
#             }
#         ]
#     },
#     {
#         "question": 'Сколько будет 3 + 3 ?',
#         "answers": [
#             {
#                 "id": '1',
#                 "value": '6',
#                 "isCorrect": True
#             }
#         ]
#     }
# ]
# mapped_data = list(map(lambda answer: 'answer', data[0]["answers"]))
# type('\n'.join(list(map(lambda answer: f'Ответ: {answer["value"]}', data[0]["answers"]))))

