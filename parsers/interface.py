from abc import ABC, abstractmethod
from . import registry
import csv, os, json, pandas

# === Декоратор-Регистратор парсеров ===
def register_parser(format_name: str):
    def decorator(cls):
        registry[format_name.lower()] = cls
        return cls
    return decorator

# === Абстрактный парсер ===
class DocumentParser(ABC):
    @abstractmethod
    def parse(self, file_path: str) -> dict:
       pass

# === Конкретные парсеры ===
@register_parser("csv")
class CSVParser(DocumentParser):
    def parse(self, file_path: str) -> dict:
        try:
            read = pandas.read_csv(file_path)
            print(read)
            print(f"CSV-файл {file_path} обработан", "кол-во строк", len(read))
        except FileNotFoundError:
            print("Ошибка: файл не найден!")
    def pars_picker(self,input1 ,input2 ,file_path: str) -> dict:
        try:
            read = pandas.read_csv(file_path)
            output = read.loc[input1:input2]
            print(output)
            print(f"CSV-файл {file_path} обработан", "кол-во строк", len(output))
        except FileNotFoundError:
            print("Ошибка: файл не найден!")
    def convert_to_json(self, file_path: str, new_file_path: str) -> dict:
        try:
            with open(file_path, newline="", encoding="utf-8") as f:
                csv_reader = pandas.read_csv(f)
                csv_reader.to_json(new_file_path, orient = "records", indent = 4, force_ascii = False)
                read = pandas.read_json(new_file_path)
                print(read)
                print(f"CSV-файл: {file_path} был обработан в json и находиться по пути: {new_file_path}.", "Кол-во строк:", len(read))
        except FileNotFoundError:
                    print("Ошибка: файл не найден!")


@register_parser("json") 
class JSONParser(DocumentParser):
    def parse(self, file_path: str) -> dict:
        try:
            read = pandas.read_json(file_path)
            print(read)
            print(f"JSON-файл {file_path} обработан", "кол-во строк", len(read))
        except FileNotFoundError:
            print("Ошибка: файл не найден!")
    
@register_parser("xlsx")
class EXCELParser(DocumentParser):
    def parse(self, file_path: str) -> dict:
        try:
            read = pandas.read_excel(file_path)
            print(read)
            print(f"XLSX-файл {file_path} обработан", "кол-во строк", len(read))
        except FileNotFoundError:
            print("Ошибка: файл не найден!")
    
# === Фабрика с доп. функционалом ===
class ParserFactory:
    @classmethod
    def create_parser(cls, format_name: str) -> DocumentParser:
        format_key = format_name.lower()
        if format_key not in registry: # Проверка наличия парсера
            available = ", ".join(registry.keys())
            raise ValueError(f"Неизвестный формат '{format_name}'. Доступно: {available}")
        return registry[format_key]()
    
    @classmethod
    def get_formats(cls) -> list:
        return list(registry.keys())
    
    @classmethod
    def parse_file(cls, file_path: str, format_name: str) -> dict:
        """Удобный метод: создает парсер и сразу парсит"""
        parser = cls.create_parser(format_name)
        return parser.parse(file_path)    