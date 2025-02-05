# python -m venv myvenv
# myvenv\Scripts\activate
# python -m pip install --upgrade pip
# pip install crewai crewai-tools
# pip install langchain_google_genai
# pip install pypdf
# pip install owlready2


from crewai.tools import tool
# from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import LLM, Agent, Task, Crew, Process
from pypdf import PdfReader
from owlready2 import *

########## LLM
# llm = ChatGoogleGenerativeAI(model="gemini/gemini-pro", temperature = 0)
llm = LLM( 
  base_url= "https://openrouter.ai/api/v1" ,
  model= "openrouter/deepseek/deepseek-r1",
  api_key= os.getenv("DEEPSEEK_API_KEY") ,
  temperature = 1.0  
)





########## TOOL1
# @tool("Leitor de PDF")
@tool('PDF Reader')
def read_pdf_tool(pdf: str) -> str:
  # """Esta ferramenta lê um arquivo em PDF retornando seu conteúdo em modo texto."""
  """This tool reads a PDF file, returning its content in text mode."""
  reader = PdfReader(pdf)
  texto = ""
  for page in reader.pages: 
    texto += page.extract_text()
  return texto

############# TESTE TOOL1
# result = read_pdf_tool._run(**{"pdf": "paper1.pdf"})
# print(result)

############# AGENT1
agent1 = Agent(
    # role="Um experiente extrator de conceitos",
    role="An experienced concept extractor",
    # goal="Analisa e interpreta complexos texto extraindo todos os conceitos relevantes sobre o tema: {topic}.",
    goal="Analyzes and interprets complex texts, extracting all relevant concepts on the topic: {topic}.",
    # backstory="Com 10 anos de experiência em análise de dados e {topic}, você se destaca em encontrar os conceitos de um texto.",
    backstory="With 10 years of experience in data analysis and {topic}, you excel at finding the concepts in a text.",
    llm=llm,
    tools=[read_pdf_tool],
    verbose=True,
    max_iter=4,
)

############# TASK1
task1 = Task(
    # description="Extrair vários conceitos sobre {topic} do arquivo {pdf} para análise subsequente.",
    description="Extract multiple concepts about {topic} from the {pdf} file for subsequent analysis.",
#    expected_output="""
#    Uma relatório contento o título do artigo analisado e uma tabela com os conceitos e um parágrafo do texto original contendo o conceito relacionado.
#    Utilize o exemplo abaixo para compor o relatório.
#    Exemplo:
#    # TÍTULO: "Título do Artigo"
#    ## Tabela de Conceitos
#    | Conceito | Contexto onde o conceito foi encontrado |
#    |-----------|----------|
#    | "Conceito achado" | "Parágrafo do texto contendo o conceito" |
#    """,
    expected_output="""
    A report containing the title of the analyzed article and a table with concepts and a paragraph of the original text containing the related concept.
    Use the example below to compose the report.
    Example:
    # TITLE: "Article Title"
    ## Concepts Table
    | Concept | Context where the concept was found |
    |-----------|----------|
    | "Found concept" | "Paragraph of the text containing the concept" |
    """,
    agent=agent1,
    output_file="concepts.md"
)




########## TOOL2
# LEITOR DE ONTOLOGIA OWL
# @tool("Leitor de Ontologia OWL")
@tool("OWL Ontology Reader")
def read_onto_tool(onto: str) -> str:
    # """Esta ferramenta lê um arquivo em OWL retornando suas classes e descrições."""
    """This tool reads an OWL file, returning its classes and descriptions."""
    onto = get_ontology(onto).load()
    # response = "CLASSES DA ONTOLOGIA E SUAS DESCRIÇÕES:\n"
    response = "CLASSES OF THE ONTOLOGY AND THEIR DESCRIPTIONS:\n"
    for cls in onto.classes():
        response = response + cls.name + " - "
        if cls.comment:
            for descricao in cls.comment: 
                response = response + descricao + " "
        response = response + ";\n"
    return response

############# TESTE TOOL2
# result = read_onto_tool._run(**{"onto": "onto.owl"})
# print(result)


############# AGENT2
agent2 = Agent(
    # role="Um experiente analista de {topic} e pesquisador de ontologia",
    role="An experienced {topic} analyst and ontology researcher",
    # goal="Relacionar conceitos de uma lista entregue por outro agente com classes de uma ontologia extraídas do arquivo {onto}. Comparando o conceito da lista e a descrição da classe.",
    goal="Relate concepts from a list provided by another agent to classes from an ontology extracted from the {onto} file. Compare the concept from the list with the description of the class.",
    # backstory="Um pesquisador de {topic} com experiência em relações ontológicas que consegue relacionar conceitos de uma lista forncecidas por outro agene e uma tabela com classes de uma ontologia do arquivo {onto} com bastante atenção aos detalhes.",
    backstory="A {topic} researcher with experience in ontological relationships who can relate concepts from a list provided by another agent and a table with classes from an ontology from the {onto} file with attention to details.",
    llm=llm,
    tools=[read_onto_tool],
    verbose=True,
    max_iter=4,
)

############# TASK2
task2 = Task(
    # description="Relacionar conceitos entregues por outro agente com as classes de uma ontologia do arquivo {onto}.",
    description="Relate concepts provided by another agent with the classes of an ontology from the {onto} file.",
#    expected_output="""
#    Um relatório formatado em markdown contendo: 
#    o título do artigo que foi entregue pelo outro agente, 
#    uma tabela dos conceitos que forma possíveis de relacionar com as classes da ontologia em uma coluna e em outra coluna uma explicação do porquê o conceito é relacionado com a classe.
#    outra tabela com os conceitos restantes da lista, quando houverem, e que não foram possíveis de relacionar com as classes da ontologia.
#    """,
    expected_output="""
    A markdown report formatted as follows:
    the title of the article provided by the other agent,
    a table of the concepts that are possible to relate with the classes of the ontology in one column and in another column an explanation of why the concept is related to the class.
    another table with the remaining concepts from the list, when there are any, that could not be related to the classes of the ontology.
    """,
    agent=agent2,
    output_file="report.md"
)




crew = Crew(
    agents=[agent1, agent2],
    tasks=[task1, task2],
    process=Process.sequential,  # or Process.hierarchical
    max_iter=10,
    full_output=True,
)

results = crew.kickoff(inputs={'topic': 'Learning Analytics', 'pdf': 'paper1.pdf', 'onto': 'onto.owl'})
print(results)

# ########## EXEMPLO DE EXECUÇÃO
# Precisa ter um arquivo .env com a variável GOOGLE_API_KEY com a chave da API do Google.
# Apenas os arquivos pdf 1,2,3 e 5 são sobre Learning Analytics.
# python crewai-onto-research.py


# Os testes de 01 até 17 foram com prompts em português.
# O teste 18 é com prompt em inglês.