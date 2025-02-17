from fpdf import FPDF
import pandas as pd

pdf=FPDF(orientation='P',unit='mm',format='A4')
df=pd.read_csv("topics.csv")

for index,row in df.iterrows():
    pdf.add_page()  # Adds new pages
    pdf.set_font(family='Times', style="B", size=24)  # Sets the page font and style
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1, border=0)
    pdf.line(10,22,200,20)

pdf.output("output.pdf")