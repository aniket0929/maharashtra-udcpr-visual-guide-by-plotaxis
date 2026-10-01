import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('ucpr_real.md', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

# 1. Front 53 notifications
notifications = []
for idx in range(35, 163):
    l = lines[idx].strip()
    m = re.match(r'^(\d+)\.\s*(.*)', l)
    if m:
        num = int(m.group(1))
        text = m.group(2)
        # Extract date if present
        date_m = re.search(r'Dated\s+([0-9]{1,2}(?:st|nd|rd|th)?\s+[A-Za-z]+,?\s+[0-9]{4}|Dt\.[0-9]{1,2}(?:st|nd|rd|th)?\s+[A-Za-z]+,?\s+[0-9]{4})', text)
        date_str = date_m.group(1) if date_m else "2020-2025"
        
        # Clean up html tags
        clean_text = re.sub(r'<[^>]+>', '', text)
        clean_date = re.sub(r'<[^>]+>', '', date_str)
        
        # Extract reference number
        ref_m = re.search(r'No\.([A-Z0-9\-\./\(\)]+)', clean_text)
        ref_no = ref_m.group(1) if ref_m else "UDD Government Order"
        
        # Determine notification type
        n_type = "Government Notification"
        if "Directives" in clean_text:
            n_type = "Directives u/s 154"
        elif "Corrigendum" in clean_text:
            n_type = "Corrigendum"
        elif "Addendum" in clean_text:
            n_type = "Addendum"
        elif "Notice" in clean_text:
            n_type = "Notice u/s 37 / 20"
        elif "Order" in clean_text:
            n_type = "Government Order"
            
        notifications.append({
            'id': num,
            'type': n_type,
            'reference': ref_no,
            'date': clean_date,
            'line_number': idx + 1,
            'description': clean_text
        })

print(f"Parsed {len(notifications)} front gazette notifications.")

# 2. Marathi Appendix Orders & Technical Annexures
marathi_orders = []
current_item = None

for idx in range(15564, len(lines)):
    l = lines[idx].strip()
    # Check for order headings
    m_order = re.search(r'^(#+\s*)(आदेश\s*क्र\.?\s*([०-९\d]+)|निदेश|शुद्धीपत्रक|परिशिष्ट|ANNEXURE\s*[-–]?\s*([A-Z0-9\-]+)?)', l, re.IGNORECASE)
    if m_order:
        tag = m_order.group(2)
        marathi_orders.append({
            'line': idx + 1,
            'heading': re.sub(r'^#+\s*', '', l),
            'tag': tag
        })

print(f"Captured {len(marathi_orders)} Marathi orders and technical annexures.")

combined_orders_data = {
    'gazette_notifications_count': len(notifications),
    'gazette_notifications': notifications,
    'appendix_orders_count': len(marathi_orders),
    'appendix_orders': marathi_orders
}

with open('data/govt_orders.json', 'w', encoding='utf-8') as f:
    json.dump(combined_orders_data, f, indent=2, ensure_ascii=False)

print("Saved data/govt_orders.json successfully.")
