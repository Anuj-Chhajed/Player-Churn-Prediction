from fpdf import FPDF
import datetime

class PDFReport(FPDF):
    def header(self):
        # Header banner
        self.set_font('Helvetica', 'B', 16)
        self.set_text_color(0, 150, 255)  # Tech Blue
        self.cell(0, 10, 'Executive Churn Intervention Plan', 0, 1, 'C')
        
        self.set_font('Helvetica', 'I', 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 6, f'Generated on: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} (AI Agentic System)', 0, 1, 'C')
        self.ln(5)
        
    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f'Page {self.page_no()} - Player Retention AI', 0, 0, 'C')

def create_pdf_report(player_id: str, prob_val: float, report_data: dict) -> bytes:
    pdf = PDFReport()
    pdf.add_page()
    
    # --- Top Metrics Level ---
    pdf.set_font("Helvetica", 'B', 12)
    pdf.set_text_color(30, 30, 30)
    pdf.cell(0, 8, f"Target Player ID: {player_id}", 0, 1)
    
    # Highlight risk level coloring
    if prob_val >= 75:
        risk_str = "CRITICAL RISK"
        pdf.set_text_color(220, 38, 38) # Red
    elif prob_val >= 40:
        risk_str = "HIGH RISK"
        pdf.set_text_color(249, 115, 22) # Orange
    else:
        risk_str = "HEALTHY"
        pdf.set_text_color(34, 197, 94) # Green
        
    pdf.set_font("Helvetica", 'B', 12)
    pdf.cell(55, 8, f"Churn Probability: {prob_val}%", 0, 0)
    pdf.cell(60, 8, f"System Class: {risk_str}", 0, 1)
    
    pdf.ln(5)
    
    # --- Profile Summary ---
    pdf.set_font("Helvetica", 'B', 14)
    pdf.set_text_color(0, 100, 200)
    pdf.cell(0, 10, "Player Profile Analysis", 0, 1)
    
    pdf.set_font("Helvetica", '', 11)
    pdf.set_text_color(50, 50, 50)
    summary_text = report_data.get('player_profile', {}).get('summary', 'No summary generated.')
    # multi_cell automatically handles word wrap
    pdf.multi_cell(0, 6, summary_text)
    
    red_flag = report_data.get('risk_analysis', {}).get('red_flag', '')
    if red_flag:
        pdf.ln(2)
        pdf.set_font("Helvetica", 'B', 11)
        pdf.set_text_color(220, 38, 38)
        pdf.multi_cell(0, 6, f"CRITICAL SIGNAL: {red_flag}")
        
    pdf.ln(8)
    
    # --- Recommendations ---
    pdf.set_font("Helvetica", 'B', 14)
    pdf.set_text_color(0, 100, 200)
    pdf.cell(0, 10, "Clean Action Cards (Recommendations)", 0, 1)
    
    recommendations = report_data.get('recommendations', [])
    if not recommendations:
        pdf.set_font("Helvetica", 'I', 11)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(0, 8, "No active interventions recommended at this time.", 0, 1)
    else:
        for rec in recommendations:
            pdf.ln(2)
            action = rec.get("action", "Unknown Action")
            prio = rec.get("priority", "Medium")
            rationale = rec.get("rationale", "")
            
            # Action title
            pdf.set_font("Helvetica", 'B', 11)
            pdf.set_text_color(30, 30, 30)
            pdf.cell(0, 6, f"- {action} [{prio.upper()} PRIORITY]", 0, 1)
            
            # Rationale text
            pdf.set_font("Helvetica", '', 10)
            pdf.set_text_color(80, 80, 80)
            pdf.multi_cell(0, 5, f"  Rationale: {rationale}")
            pdf.ln(2)
            
    # --- Output Bytes ---
    # fpdf2's output() without a name argument returns a bytearray natively
    return bytes(pdf.output())
