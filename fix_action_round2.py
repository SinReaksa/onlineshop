from pathlib import Path
import re
path = Path('action.php')
text = path.read_text(encoding='utf-8')
# Insert null-safe avg_count handling after avg_rating assignment, once per occurrence.
old = r'(\$avg_count=\$review_row\["avg_rating"\];)'
insert = r"\1\n                                                $avg_count = is_numeric($avg_count) ? floatval($avg_count) : 0;\n                                                $filledStars = round($avg_count);\n                                                $emptyStars = max(0, 5 - $filledStars);"
text, n1 = re.subn(old, insert, text)
text, n2 = re.subn(r'while\(\$i <= round\(\$avg_count\)\)\{', 'while($i <= $filledStars){', text)
text, n3 = re.subn(r'while\(\$i <= 5-round\(\$avg_count\)\)\{', 'while($i <= $emptyStars){', text)
path.write_text(text, encoding='utf-8')
print(f'replaced avg_count insert: {n1}, round1: {n2}, round2: {n3}')
