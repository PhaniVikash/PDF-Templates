from fpdf import FPDF
import pandas as pd

pdf=FPDF(orientation='P',unit='mm',format='A4')
df=pd.read_csv("topics.csv")
pdf.set_auto_page_break(margin=0,auto=False)

for index,row in df.iterrows():
    pdf.add_page()  # Adds new pages
    #Set Header
    pdf.set_font(family='Times', style="B", size=24)  # Sets the page font and style
    pdf.set_text_color(139,0,0)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1, border=0)
    pdf.line(10,22,200,22)

    #Set Footer
    pdf.ln(262)
    pdf.set_font(family="Times",style="I",size=8)
    pdf.set_text_color(180,180,180)
    text=row['Topic']+"  page : "+str(row["Order"])
    pdf.cell(txt=text,align="R",w=0,h=8,border=0)


    for i in range(row['Pages']-1):
        pdf.add_page()
        # Set Footer
        pdf.ln(276)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        text = row['Topic'] + "  page : " + str(row["Order"]+1)
        pdf.cell(txt=text, align="R", w=0, h=8, border=0)




pdf.output("output.pdf")