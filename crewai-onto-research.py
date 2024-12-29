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
  api_key=os.getenv("GOOGLE_API_KEY"),
  model="gemini/gemini-pro",
  temperature = 0.0                      # 0.0 - 1.0 para o modelo gemini/gemini-pro
)





########## TOOL1
@tool("Leitor de PDF")
def read_pdf_tool(pdf: str) -> str:
  """Esta ferramenta lê um arquivo em PDF retornando seu conteúdo em modo texto."""
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
    role="Um experiente analisador de dados",
    goal="Analisa e interpreta complexos artigos científicos extraindo conceitos relevantes sobre o tema: {topic}.",
    backstory="Com 10 anos de experiência em análise de dados e {topic}, você se destaca em encontrar os conceitos chaves de um texto.",
    llm=llm,
    tools=[read_pdf_tool],
    verbose=True,
    max_iter=4,
)

############# TASK1
task1 = Task(
    description="Extrair vários conceitos relevantes sobre {topic} do arquivo {pdf} para análise subsequente.",
    expected_output="""
    Uma relatório contento o título do artigo analisado e uma tabela com os conceitos e um parágrafo do texto original contendo o conceito relacionado.
    Utilize o exemplo abaixo para compor o relatório.
    Exemplo:
    # Título do Artigo
    ## Tabela de Conceitos
    | Conceito | Contexto |
    |-----------|----------|
    | "Conceito achado" | "Parágrafo do texto contendo o conceito" |
    """,
    agent=agent1,
    output_file="concepts.md"
)




########## TOOL2
# LEITOR DE ONTOLOGIA OWL
@tool("Leitor de Ontologia OWL")
def read_onto_tool(onto: str) -> str:
    """Esta ferramenta lê um arquivo em OWL."""
    onto = get_ontology(onto).load()
    response = "CLASSES DA ONTOLOGIA:\n"
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
    role="Um experiente analista de {topic} e pesquisador de ontologia",
    goal="Consegue relacionar conceitos de uma lista entregue por outro agente com classes de uma ontologia extraídas do arquivo {onto}.",
    backstory="Um pesquisador de {topic} com experiência em pesquisa científica e conhecimento em ontologia que consegue relacionar conceitos de uma tabela com classes de uma ontologia do arquivo {onto} com bastante atenção aos detalhes.",
    llm=llm,
    tools=[read_onto_tool],
    verbose=True,
    max_iter=4,
)

############# TASK2
task2 = Task(
    description="Relacionar conceitos entregues por outro agente com as classes de uma ontologia.",
    expected_output="""
    Um relatório formatado em markdown contendo: 
    o título do artigo que foi entregue pelo outro agente, 
    uma tabela dos conceitos que forma possíveis de relacionar com as classes da ontologia e 
    outra tabela com os conceitos que não foram possíveis de estabelecer um relacionamento, quando houverem.
    """,
    agent=agent2,
    output_file="report.md"
)




crew = Crew(
    agents=[agent1, agent2],
    tasks=[task1, task2],
    process=Process.sequential,  # or Process.hierarchical
    max_iter=4,
    full_output=True,
)

results = crew.kickoff(inputs={'topic': 'Learning Analytics', 'pdf': 'paper1.pdf', 'onto': 'onto.owl'})
print(results)