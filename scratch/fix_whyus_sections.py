with open('pages/why-us.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('<section class="section" style="background: var(--clr-white);">', '<section class="section why-fs" style="background: var(--clr-white);">')
c = c.replace('<section class="section" style="background: #F8FAFC;">', '<section class="section why-fs" style="background: #F8FAFC;">')
c = c.replace('<section class="section" style="background: #F0F7FF;">', '<section class="section why-fs" style="background: #F0F7FF;">')
c = c.replace('<section class="section">', '<section class="section why-fs">')

with open('pages/why-us.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Done - added why-fs class')
