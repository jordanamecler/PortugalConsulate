# Consulate of Portugal in Rio de Janeiro's Crawler
EN  
This script periodically crawls the Consulate of Portugal in Rio de Janeiro's website to check if new spots are available for civil registry appointments.  
The motivation for implementing this crawler comes from the difficulty in finding opened spots for these appointments. Using this script will allow you to be notified whenever new spots are available.  
Written in *Python* using [Selenium](https://www.selenium.dev/) for automation.
### Step by step
+ Execute script from terminal with `python agendamento.py`
+ Enter your CPF as requested
+ Enter your password from the consulate's website as requested

The script will then run periodically (every 5 minutes) to check if there are any opened spots for appointments for the civil registry service. If there are no spots available, it will print on terminal the date and time saying there are no spots, otherwise it will print on terminal and emit a sound on the computer saying there are new spots.

PT  
Este script acessa periodicamente o site do Consulado de Portugal do Rio de Janeiro para checar se há novas vagas para agendamento de registro civil.  
A motivação para a implementação deste crawler vem da dificuldade em achar vagas abertas para estes agendamentos. Este script permitirá que você seja notificado quando novas vagas estiverem disponíveis.
Desenvolvido em *Python* utilizando [Selenium](https://www.selenium.dev/) para automação.
### Passo a passo
+ Execute o script a partir do terminal com `python agendamento.py`
+ Digite seu CPF como solicitado
+ Digite sua senha do site do consulado como solicitado

O script rodará periodicamente (a cada 5 minutos) checando se há novas vagas para agendamento no serviço de registro civil. Se não houver vagas disponíveis, exibirá no terminal a data e hora e uma mensagem de que não há vagas. Caso contrário, exibirá no terminal e emitirá um som no computador dizendo que há novas vagas.