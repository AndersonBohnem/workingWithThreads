# workingWithThreads

Este código utiliza threads para gerenciar a abertura e o fechamento de múltiplas instâncias do Notepad no Windows. Duas threads são criadas para abrir Notepads, com um intervalo de 10 segundos entre cada abertura. Um contador global rastreia quantos Notepads foram abertos, e um lock é usado para garantir que o contador seja atualizado de forma segura, evitando problemas de concorrência. Após abrir todas as instâncias, uma terceira thread é iniciada para fechar todas as janelas do Notepad após 15 segundos, utilizando o comando taskkill. As threads permitem que as instâncias sejam abertas em paralelo, sem bloqueio de execução, e o lock assegura que o acesso ao contador seja sincronizado, evitando condições de corrida. Como resultado, o código abre os Notepads, registra o horário de abertura e, 15 segundos depois, fecha todas as janelas, demonstrando um gerenciamento eficiente e organizado das operações.