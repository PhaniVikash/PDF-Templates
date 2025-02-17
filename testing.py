from fpdf import FPDF

pdf=FPDF(orientation="P")

def foo():
    pdf.add_page()  # Adds new pages
    pdf.set_font(family='Times', style="B", size=12)  # Sets the page font and style
    pdf.cell(w=0, h=12, txt="This is first line ", align="L", ln=1, border=1)
    pdf.cell(w=0, h=12, txt="This is 2nd line ", align="L", ln=1, border=1)
    pdf.cell(w=0, h=12, txt="Boarder Removed ", align="L", ln=1, border=0)
    pdf.cell(w=0, h=12, txt="Align set to R   ", align="R", ln=1, border=1)
    pdf.cell(w=50, h=12, txt="W set to 50 ", align="L", ln=1, border=1)
    pdf.cell(w=0, h=30, txt="h set to 20", align="L", ln=1, border=1)
    pdf.cell(w=0, h=12, txt="All tested", align="L", ln=1, border=1)