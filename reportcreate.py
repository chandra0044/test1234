# Reading html template
files = open('report.html', 'r')
# Saving output html
output2 = open('StyleCop_Output.html','w')
xmlfile = open('StylecopResults_AuditService22.xml','r')
xmlfile2 = open('StylecopResults_AuditService.xml','w')
i=1
for line2 in xmlfile:
    line2 = line2.replace('>', '\n')
    print(line2)
    xmlfile2.write(line2)

xmlfile2 = open('StylecopResults_AuditService.xml','r')
for linehtml in files:
    output2.write(linehtml)
    if '<div class="log">' in linehtml:
        for line in xmlfile2:
            line = line.replace('<StyleCopViolations>', '')
            line = line.replace('</StyleCopViolations>', '')
            line = line.replace('<Violation', '<pre><code>')
            line = line.replace('</Violation>', '</code></pre>')
            if '</Violation' not in line:
                line = line.replace(' ', '<br>')
            output2.write(line)
    i=i+1

xmlfile2.close()
output2.close()
