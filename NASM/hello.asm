section .data
    hello db 'Hello, World!', 0

section .text
    global main
    extern ExitProcess, GetStdHandle, WriteConsoleA

main:
    ; Получаем стандартный вывод (stdout)
    push -11             ; STD_OUTPUT_HANDLE
    call GetStdHandle
    mov rbx, rax         ; дескриптор стандартного вывода

    ; Печатаем строку
    push 0               ; lpNumberOfCharsWritten (не используем, передаем 0)
    push 13              ; количество символов для печати (длина строки)
    push offset hello    ; строка для вывода
    push rbx             ; дескриптор stdout
    call WriteConsoleA

    ; Завершаем программу
    push 0
    call ExitProcess
