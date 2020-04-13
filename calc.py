print("Calculo de taxação p site")
print("")

pv = float(input("Digite o valor de venda do produto : "))
pp = float(input("Digite o preço de produção p/ unid : "))
print("")
dlr = float(input("""Digite o valor atual do dolar ou digite
0 (zero) p/ definir 1$ como R$5.11 : """))
print("")
s_n = str(input("Pagar taxa de 2 meses s/ juros ? s/n "))
dom_str = str(input("vamos pagar o dominio este mes ? s/n "))
print("")

pcl_crd = pv * 0.02
pct_shp = pv * 0.03
pct_crd = pv * 0.05
txf_shp = dlr * 0.3
jrs = pv * 0.025
dom = 0

if  dlr == 0:
    dlr = 5.11

if dom_str == "s" or dom_str == "S" or dom_str == "sim" or dom_str == "SIM":
    dom = 40
if dom_str == "n" or dom_str == "N" or dom_str == "nao"or dom_str == "NAO":
    dom = 0

if s_n == "s" or s_n == "S" or s_n == "sim" or s_n == "SIM":
    lpp = pv - pp - pct_shp - pct_crd - txf_shp - jrs
    msl = dlr * 30 + dom 
    qtd = msl / lpp
    mrg =  pv / lpp * 100
    print("O lucro por venda é : {:.2f}".format(lpp))
    print("")
    print("""Precisamos vender {:.2f} unidades para
pagar R${:.2f} de manutenção do site""".format(qtd,msl))
    print("")
    print("A margem de lucro corresponde a : {:.2f}%".format(mrg))  

elif s_n == "n" or s_n == "N" or s_n == "nao" or s_n == "NAO":

    lpp = pv - pp - pct_shp - pct_crd - txf_shp  
    msl = dlr * 30 + dom
    qtd = msl / lpp
    mrg =  pv / lpp * 100
    print("O lucro por unidade vendida é : {:.2f}".format(lpp))
    print("")
    print("""Precisamos vender {:.2f} mascaras para
pagar R${:.2f} de manuteção do site.""".format(qtd,msl))
    print("")
    print("A margem de lucro corresponde é : {:.2f}%".format(mrg))

else :
    print("Comando não reconhecido, tente novamente !")

print("")

fim = str(input("Finalizar!"))
