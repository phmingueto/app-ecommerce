# class engine2:
#     @staticmethod
#     def modify_column(column_condition, column_modified, modify, dataframe):
#         dataframe.loc[dataframe,f'{}'column_condition, f'{}', column_modified] = modify
from src.application.elt.etl import Engine

dictt = {'Roupa De Mergulho Surf 3mm Longa Preta Masculina Promoção': 'ROUPAMERG3MM',
         'Aparelho Lipocavitação Rádio Frequência Ultra 40k': 'LIPOCAV',
         'Adaptador Hub Usb-c 3.1 P/ Usb Hdmi Usb-c P/ Mackbook': 'HUB',
         'Massageador Phoenix A2 Hypervolt Pronta Entrega Maleta': 'MASPHOA2',
         'Modem Roteador 3g E 4g C/ Chip Sim Portátil Desbloqueado': 'ROT3GPORTATIL',
         'Amplificador Repetidor De Sinal De Celular 2100mhz Cb': '2100CB',
         'Amplificador Repetidor De Sinal De Celular 850mhz 2g/3g/4g': '850L',
         'Adaptador Hub Usb-c 3.1 Para Usb Hdmi Sd Usb-c P/ Mackbook': 'HUB',
         'Acionador De Fogos  Gerbs Sem Fio 12 Canais Modo Sequencial': 'ACIONADOR',
         'Fone Bluetooth A900 Tws Geração 3 Pronta Entrega': 'FONETWS3',
         'Depilador A Laser Profissional 900 Mil Dis. Flash Original': 'DEPIL900',
         'Modem Roteador 3g E 4g C/ Chip Antena Desbloqueado': 'ROTANTENA',
         'Massageador Phoenix A2 Novo Original + Ponteiras Original': 'MASPHOA2',
         'Amplificador Repetidor De Sinal De Celular 850mhz Cb': '850CB',
         'Mixer Mesa De Som 4 Canais Com Bluetooth Usb Rca Promoção': 'MIXER4C',
         'Fone A900 Tws Novo O Melhor Pronta Entrega': 'FONETWS3',
         'Air Pods 3 Tws O Melhor Promoção Pronta Entrega': 'FONETWS3',
         'Bomba Submersa 12v Transferência Óleo Diesel Água': 'BOMBSUB12V',
         'Controlador Timer Fluxo Água - Temporizador Irrigação': 'AGUATEMP',
         'Amplificador Repetidor De Sinal De Celular 700 Mhz Cb': '700CB',
         'Amplificador Repetidor De Sinal De Celular 2600mhz Cb': '2600CB',
         'Smartwatch Iwo 13 W56 Original C/ Pulseira Capinha Promoção': 'IWOW56PRET40',
         'AirPods 3 Tws O Melhor Promoção Pronta Entrega': 'FONETWS3',
         'Amplificador Repetidor De Sinal De Celular 900 Mhz Cb': '900CB'}



engine = Engine
df = engine.extract(pasta=rf"\Users\\PEDRO\Downloads\res_financeiro.xlsx")

# for k, v in dictt.items():
#     df.loc[df.tituloItem == k, 'SkuProduto'] = v

modify_column = engine.modify_column(dataframe=df, dictt=dictt, column_key='tituloItem', column_value='SkuProduto')

engine.write(pasta=rf'\Users\\PEDRO\Downloads', dataframe=df, file='res_financeiro.xlsx')





