from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        epw = self.w - (2 * self.l_margin)
        self.set_font('helvetica', 'B', 40)
        self.cell(0, 60, 'CS50 Shirtificate', align = 'C')

        self.image('shirtificate.png', 10, 80, w = epw)


    def writeline(self, name):
        self.set_font('helvetica', '', 30)
        self.set_text_color(255,255,255)
        self.text(55, 150, f'{name} took CS50')


def main():
    name = input('Name: ')
    pdf = PDF()
    pdf.add_page()
    pdf.writeline(name)

    pdf.output('shirtificate.pdf')


if __name__ == '__main__':
    main()