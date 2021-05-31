class Solution:
  def reorderLogFiles(self, logs: List[str]) -> List[str]:
    digits = []
    letters = []
    for entry in logs:
        if entry[-1].isdigit():
            digits.append(entry)
        else:
            letters.append(entry)
    letters.sort(key=lambda x: x.split()[0])
    letters.sort(key=lambda x: x.split()[1:])
    final = letters + digits
    return final
