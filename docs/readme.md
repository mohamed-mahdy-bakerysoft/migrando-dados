### Projeto Migração de dados

### Orientações:

Na pasta “Teste Prático” existem três arquivos:
1.	Orientações para o teste (Orientações para migração.docx)
2.	Base do Escritório (Backup_de_dados_92577.rar)
3.	Modelo de tabelas XPTO (pasta XPTO)

Siga as instruções abaixo para realização do teste.

É importante saber que o intuito principal de nosso procedimento é trazer todos os dados possíveis do cliente para a XTPO.

Você executará o procedimento do departamento jurídico responsável pelo Escritório 92577.

Para definirmos se são dados de migração ou não, utilizamos as nossas planilhas padrões (Pasta XPTO). Nela inserimos os dados, contidos na base Backup_de_dados_92577, através da realização de todos os vínculos necessários entre as tabelas. Use as colunas a seu favor! 

As planilhas padrões contêm instruções fundamentais para migração. Por exemplo, as datas devem ser inseridas no formato nacional, sendo DD/MM/AAAA.
Atenção para campos obrigatórios.

* Clientes

A tabela de clientes contém todos os contatos do escritório. Ela possui informações como telefone, celular, endereço, e-mail, etc. Todas as pessoas vinculadas em um processo estão contidas nessa tabela.

* Processos

Aqui você encontrará todos os processos desse escritório. Os processos que não possuem nenhum número são do grupo administrativo e todos os que não possuírem 20 (sem máscaras) /25 caracteres (com máscaras) são extrajudiciais.

Nome dos clientes, Parte contrária devem ser o mesmo em ambas as planilhas.
Ao preencher as colunas, elabore um update unindo as tabelas necessárias para que retorne o conteúdo correto de acordo com o relacionamento correspondente.

Assim, elabore um código computacional, em linguagem de programação Python, que irá trazer os dados, necessários e suficientes, das tabelas contidas na Base do Escritório, para a migração. Dica: nem todos são! Ainda assim, lembre-se de trazer a maior quantidade de informação possível.

Após, também via linguagem Python, realize o tratamento dos dados obtidos (saneamento, estruturação, formatação, padronização, ...) de acordo com o tipo de cada tabela modelo da XPTO. A ideia é realizar esse tratamento para que o Escritório tenha a melhor experiência possível com a migração.

Por fim, desenvolva uma interface de operação, por mais simples que seja, porém precisa ser intuitiva, para que o operador possa subir a base do Backup e obter, ao final da execução do código, o download dos arquivos já no modelo de tabelas XPTO com todos os dados de Clientes e Processos correspondentes ao Escritório 92577.


