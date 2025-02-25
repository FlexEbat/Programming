#include <iostream>
#include <fstream>
#include <string>

int main()
{
    std::string filename = "out.txt";

    // Проверка на наличие файла
    std::ifstream file(filename);
    if (!file.is_open())
    {
        std::cerr << "Файл " << filename << " не найден!" << std::endl;
        return 1; // Прекратить выполнение программы
    }

    // Если файл открыт, считываем и отображаем его содержимое
    std::string line;
    while (std::getline(file, line))
    {
        std::cout << line << std::endl;
    }

    file.close(); // Закрываем файл

    return 0;
}

// g++ pizda.cpp - o main2