from pathlib import Path
import re
path = Path('body.php')
text = path.read_text(encoding='utf-8')
text_before = text
text = re.sub(
    r'(\$avg_count=\$review_row\["avg_rating"\];)(\s*\n)',
    r"\1\n\t\t\t\t\t\t\t\t\t$avg_count = is_numeric($avg_count) ? floatval($avg_count) : 0;\n\t\t\t\t\t\t\t\t\t$filledStars = round($avg_count);\n\t\t\t\t\t\t\t\t\t$emptyStars = max(0, 5 - $filledStars);\2",
    text,
)
text = text.replace('while($i <= round($avg_count))', 'while($i <= $filledStars)')
text = text.replace('while($i <= 5-round($avg_count))', 'while($i <= $emptyStars)')
path.write_text(text, encoding='utf-8')
print('modified' if text != text_before else 'no changes')
