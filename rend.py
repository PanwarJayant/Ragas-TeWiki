import pickle
import pandas as pd
import ast
from jinja2 import Environment, FileSystemLoader

from genXML import tewiki, writePage


def getData(row):
    data = {
        'regional_name': row[0],
        'aro': ast.literal_eval(row[1]),
        'ava': ast.literal_eval(row[2]),
        'aro_swaras': ast.literal_eval(row[3]),
        'ava_swaras': ast.literal_eval(row[4]),
        'kritis': ast.literal_eval(row[5]),
        'aro_seq': row[6],
        'ava_seq': row[7],
        'category': row[8],
        'swaras': ast.literal_eval(row[9]),
        'melam_num': str(row[10]),
        'janaka_melam': row[11],
        'janaka': row[12],
        'chakra': row[13],
        'chakra_num': str(row[14]),
        'hind': ast.literal_eval(row[15]),
        'songs': ast.literal_eval(row[16]),
        'alternates': ast.literal_eval(row[17]),
        'same_aro': ast.literal_eval(row[18]),
        'same_ava': ast.literal_eval(row[19]),
        'one_swara_diff': ast.literal_eval(row[20]),
        'varnams': ast.literal_eval(row[21])
    }

    return data


def main():
    file_loader = FileSystemLoader('./')
    env = Environment(loader=file_loader)
    template = env.get_template('Bing-Translate/bing.j2')
    moviesDF = pd.read_pickle(open('./123.pkl', 'rb'))
    
    fobj = open('ragas_google.xml', 'w')
    fobj.write(tewiki+'\n')

    initial_page_id = 700000

    for i in range(0, 50):
        row = moviesDF.iloc[i]
        text = template.render(getData(row))
        stri = "./Bing-Translate/articles/" + str(i) + ".txt"
        writePage(initial_page_id,row[0],text,fobj)
        initial_page_id += 1
        # file = open(stri, "w")
        # file.write(text)
        # file.close

    fobj.write('</mediawiki>')
    fobj.close()

if __name__ == '__main__':
    main()
