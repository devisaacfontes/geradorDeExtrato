import pandas as pd
from fpdf import FPDF

dados = {
    'data': ['2025-06-02', '2025-06-03', '2025-06-07'],
    'descricão': ['deposito', 'pagamento conta de luz', 'saque'],
    'valor': [1500.00, -230.00, -500.00]
}

df = pd.DataFrame(dados)

df['Saldo Acumulado'] = df['valor'].cumsum()

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Extrato Bancario", ln=True, align='C')

pdf.set_font("Arial", '', 12)
pdf.ln(10)  # espaço

pdf.cell(40, 10, "Data", 1)
pdf.cell(80, 10, "Descrição", 1)
pdf.cell(30, 10, "Valor", 1)
pdf.cell(40, 10, "Saldo", 1)
pdf.ln()

for index, row in df.iterrows():
    pdf.cell(40, 10, row['data'], 1)
    pdf.cell(80, 10, row['descricão'], 1)
    pdf.cell(30, 10, f"R$ {row['valor']:.2f}", 1)
    pdf.cell(40, 10, f"R$ {row['Saldo Acumulado']:.2f}", 1)
    pdf.ln()

pdf.output("extrato_bancario.pdf")

print("Extrato Bancario gerado com sucesso")
