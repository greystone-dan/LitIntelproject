import sqlite3
conn = sqlite3.connect(r'C:\Users\danny\OneDrive\Desktop\AI CaseLibrary\data\raw\fc\fc_decisions.db')
cur = conn.cursor()
print(cur.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall())
print('fc_decisions', cur.execute('SELECT COUNT(*) FROM fc_decisions').fetchone()[0])
print('fc_pdfs', cur.execute('SELECT COUNT(*) FROM fc_pdfs').fetchone()[0])
print('latest', cur.execute('SELECT fc_id, neutral_citation, decision_date, item_url FROM fc_decisions ORDER BY rowid DESC LIMIT 5').fetchall())
