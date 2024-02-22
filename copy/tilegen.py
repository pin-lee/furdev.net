def generate(header, description, stack):
    return f"""
        <div class="item">
            <img src="">
            <div class="item_text">
            <h2>{header}</h2>
                <i>{stack}</i>
                <p>{description}</p>
            </div>
        </div>"""

source = open('index.html', 'r')
lines = source.readlines()

output = ""

for i in range(0, len(lines), 3):
    output += generate(
        lines[i].replace('\n', ''), 
        lines[i+1].replace('\n', ''), 
        lines[i+2].replace('\n', ''))

source.close()

file = open('output.html', 'w+')
file.write(output)
file.close()