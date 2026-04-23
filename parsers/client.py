from .interface import  ParserFactory

# # Получаем и используем парсер
# prs = ParserFactory.create_parser('csv')
# res = prs.parse('./files/data.csv')
# print(res)

# # Получаем список доступных парсеров
# print(ParserFactory.get_formats())

# # Парсим указанный файл
# print(ParserFactory.parse_file('./files/data.csv','csv'))

# prs = ParserFactory.create_parser('xlsx')
# res = prs.parse('./files/data1.xlsx')
# print(res)

# prs = ParserFactory.create_parser('csv')
# res = prs.pars_picker(3,4,'./files/data.csv')
# print(res)

# prs = ParserFactory.create_parser('csv')
# res = prs.convert_to_json('./files/data.csv', './files/data.json')
# print(res)

# prs = ParserFactory.create_parser('csv')
# res = prs.last_row('./files/data.csv')
# print(res)

prs = ParserFactory.create_parser('csv')
res = prs.row_filter('fam',"=",'1','./files/data.csv')
print(res)