#!/usr/bin/python 
# -*- coding: utf-8 -*-

from py2neo import Node, Relationship, Graph , authenticate
#authenticate("localhost:7474", "neo4j", "neo4j")
graph = Graph("http://localhost:7474/db/data/")
# détruit les noeuds existants
graph.delete_all()
col=Node("UE3",nom="COL",cm=0,cmtd=6,td=0,tp=2,total=8,enseignants="POUCHOULON Jean-Marc",intitule="Collecte de Logs")
graph.create(col)
fwl=Node("UE2",nom="FWL",cm=0,cmtd=6,td=0,tp=2,total=8,enseignants="BORELLY Christophe",intitule="Base des Firewalls")
graph.create(fwl)
ip6=Node("UE2",nom="IP6",cm=0,cmtd=6,td=0,tp=2,total=8,enseignants="GOMEZ Rene",intitule="Internet protocol version 6")
graph.create(ip6)
lan=Node("UE2",nom="LAN",cm=0,cmtd=3,td=0,tp=1,total=4,enseignants="HUGUES Guillaume",intitule="Base des réseaux locaux")
graph.create(lan)
hyp=Node("UE2",nom="HYP",cm=0,cmtd=6,td=0,tp=2,total=8,enseignants="OLIVES Lionel",intitule="hyperfrequence")
graph.create(hyp)
htr=Node("UE2",nom="HTR",cm=0,cmtd=12,td=0,tp=4,total=16,enseignants="PODLUNSEK Vincent",intitule="Environnements hétérogènes")
graph.create(htr)
afp=Node("UE3",nom="AFP",cm=0,cmtd=6,td=0,tp=2,total=8,enseignants="MANTEAU Julien",intitule="Firewalls avancés")
graph.create(afp)
sup=Node("UE3",nom="RPO",cm=0,cmtd=6,td=0,tp=2,total=8,enseignants="POUCHOULON Jean-Marc",intitule="Supervision")
graph.create(sup)
bkp=Node("UE3",nom="BKP",cm=0,cmtd=6,td=0,tp=2,total=8,enseignants="SALOMON Dominique",intitule="Politique de Sauvegarde")
graph.create(bkp)
cry=Node("UE2",nom="CRY",cm=2,cmtd=5,td=0,tp=3,total=10,enseignants="PUJAS Philippe",intitule="Cryptographie")
graph.create(cry)
isi=Node("UE2",nom="ISI",cm=0,cmtd=6,td=0,tp=2,total=8,enseignants="DRUON Sébastien",inititule="Insécurité des systèmes d'informations")
graph.create(isi)
exc=Node("UE3",nom="EXC",cm=0,cmtd=6,td=0,tp=2,total=8,enseignants="BONMARCHAND Marc",intitule="Environnement Collaboratif")
graph.create(exc)
ssh=Node("UE2",nom="SSH",cm=0,cmtd=6,td=0,tp=2,total=8,enseignants="ARNAUD Antoine",intitule="Shell Sécurisé")
graph.create(ssh)
eng=Node("UE1",nom="ENG",cm=0,cmtd=10,td=0,tp=0,total=10,enseignants="MICHAUD Didier",intitulé="Anglais")
graph.create(eng)
pgp=Node("UE3",nom="PGP",cm=0,cmtd=5,td=0,tp=2,total=7,enseignants="BORELLY Christophe",intitule="Pretty Good Privacy")
graph.create(pgp)
vrt=Node("UE2",nom="VRT",cm=0,cmtd=9,td=0,tp=3,total=12,enseignants="POUCHOULON Jean-Marc",intitule="Virtualisation")
graph.create(vrt)
tel=Node("UE2",nom="TEL",cm=0,cmtd=12,td=0,tp=4,total=16,enseignants="PUJAS Agnes",intitule="Base de la téléphonie")
graph.create(tel)
rdyn=Node("UE3",nom="RDYN",cm=0,cmtd=6,td=0,tp=2,total=8,enseignants="PLESSIS Benoit",intitule="Routage dynamique")
graph.create(rdyn)
ce=Node("UE1",nom="CE",cm=0,cmtd=15,td=0,tp=0,total=15,enseignants="PENA Guillaume",intitule="Culture d'entreprise")
graph.create(ce)
pre=Node("UE0",nom="PRE",cm=0,cmtd=0,td=0,tp=0,total=45,enseignants="POUGET Daniel,Z KNOMY Oto,GALY Jerome",intitule="Projets")
graph.create(pre)
web=Node("UE3",nom="WEB",cm=0,cmtd=6,td=0,tp=2,total=8,enseignants="SANCHEZ David",intitule="Frontaux Web")
graph.create(web)
wan=Node("UE2",nom="WAN",cm=0,cmtd=0,td=0,tp=0,total=2,enseignants="GARCIA Ronnie",intitule="Réseaux FAI")
graph.create(wan)
mal=Node("UE3",nom="MAL",cm=0,cmtd=6,td=0,tp=2,total=8,enseignants="LIQUIERE Michel",intitule="Malware")
graph.create(mal)
tse=Node("UE3",nom="TSE",cm=0,cmtd=4,td=0,tp=1,total=5,enseignants="PODLUNSEK Vincent",intitule="")
graph.create(tse)
ip4=Node("UE2",nom="IP4",cm=0,cmtd=6,td=0,tp=2,total=8,enseignants="BORELLY Christophe",intitule="Reseaux IPV4")
graph.create(ip4)
ins=Node("UE0",nom="INS",cm=0,cmtd=5,td=0,tp=0,total=5,enseignants="CASTEL Victor",intitule="Installation Debian")
graph.create(ins)
cisco=Node("UE",nom="CISCO",cm=0,cmtd=0,td=0,tp=0,total=6,enseignants="non affecté",intitule="Cours Cisco R&S1")
graph.create(cisco)
tun=Node("UE2",nom="TUN",cm=0,cmtd=6,td=0,tp=2,total=8,enseignants="ARNAUD Antoine",intitule="Tunnel")
graph.create(tun)
mgt=Node("UE1",nom="MGT",cm=0,cmtd=9,td=0,tp=0,total=9,enseignants="PRATALI Anne",intitule="Management")
graph.create(mgt)
win=Node("UE3",nom="WIN",cm=0,cmtd=12,td=0,tp=4,total=16,enseignants="BONMARCHAND Marc",intitule="Serveurs Windows")
graph.create(win)
sec=Node("UE3",nom="SEC",cm=0,cmtd=2,td=3,tp=0,total=5,enseignants="PUJAS Philippe",intitule="Sécurité Informatique")
graph.create(sec)
adns=Node("UE3",nom="ADNS",cm=0,cmtd=4,td=0,tp=1,total=5,enseignants="BORELLY Christophe",intitule="DNS avancé")
graph.create(adns)
gp=Node("UE1",nom="GP",cm=0,cmtd=11,td=0,tp=0,total=11,enseignants="POUGET Daniel,GALY Jerome,TEXIER-DECLERCK Veronique",intitule="Gestion de projets")
graph.create(gp)
com=Node("UE1",nom="COM",cm=0,cmtd=12,td=0,tp=3,total=15,enseignants="FACERIAS Sophie",intitule="Communication")
graph.create(com)
dns=Node("UE2",nom="DNS",cm=0,cmtd=6,td=0,tp=2,total=8,enseignants="PLESSIS Benoit",intitule="DNS")
graph.create(dns)
pki=Node("UE3",nom="PKI",cm=0,cmtd=4,td=0,tp=1,total=5,enseignants="SANCHEZ David",intitule="Infrastructure clefs publiques")
graph.create(pki)
lin=Node("UE2",nom="LIN",cm=0,cmtd=12,td=0,tp=4,total=16,enseignants="POUCHOULON Jean-Marc",intitule="Environnement Linux")
graph.create(lin)
net=Node("UE0",nom="NET",cm=0,cmtd=18,td=0,tp=6,total=24,enseignants="ARNAUD Antoine",intitule="Bases des réseaux")
graph.create(net)
afo=Node("UE3",nom="AFO",cm=0,cmtd=6,td=0,tp=2,total=8,enseignants="PODLUNSEK Vincent",intitule="")
graph.create(afo)
ged=Node("UE3",nom="GED",cm=0,cmtd=0,td=0,tp=0,total=3,enseignants="PODLUNSEK Vincent",intitule="Gestion Electronique de Document")
graph.create(ged)
vdi=Node("UE2",nom="VDI",cm=0,cmtd=1,td=0,tp=0,total=1,enseignants="FACERIAS Michel",intitule="Voix, Données, Images")
graph.create(vdi)
mail=Node("UE3",nom="MAIL",cm=0,cmtd=9,td=0,tp=3,total=12,enseignants="POUCHOULON Jean-Marc",intitule="Infrastructure et Sécurité de la messagerie")
graph.create(mail)
shl=Node("UE0",nom="SHL",cm=0,cmtd=22,td=0,tp=8,total=31,enseignants="PUJAS Philippe,non affecté,CASTEL Victor",intitule="Shell")
graph.create(shl)
#do=Node("UE1",nom="DO",cm=0,cmtd=6,td=0,tp=0,total=6,enseignants="CARRIE Stephanie",intitule="Droit des obligations")
#graph.create(do)
dir=Node("UE2",nom="DIR",cm=0,cmtd=6,td=0,tp=2,total=8,enseignants="COMBY Frederic",intitule="Annuaires LDAP")
graph.create(dir)
cm=Node("UE1",nom="CM",cm=3,cmtd=0,td=0,tp=0,total=3,enseignants="COMMERCON Fredéric",intitule="Culture Métier")
graph.create(cm)
di=Node("UE1",nom="DI",cm=0,cmtd=6,td=0,tp=0,total=6,enseignants="CARRIE Stephanie",intitule="Droit de l'informatique")
graph.create(di)
dpl=Node("UE2",nom="DPL",cm=0,cmtd=12,td=0,tp=4,total=16,enseignants="DUBREUIL Eric",intitule="Déploiement et automatisation")
graph.create(dpl)
wlan=Node("UE2",nom="WLAN",cm=0,cmtd=9,td=0,tp=3,total=12,enseignants="OLIVES Lionel",intitule="Réseaux sans fil")
graph.create(wlan)
pyn=Node("UE2",nom="PYN",cm=0,cmtd=15,td=0,tp=9,total=24,enseignants="Jean-Marc Pouchoulon",intitule="Python pour les réseaux et systèmes",graine="OUI")
graph.create(pyn)
cad=Node("UE2",nom="CAP",cm=0,cmtd=5,td=0,tp=3,total=8,enseignants="Jean-Marc Pouchoulon",intitule="Containers Applicatifs Docker",graine="OUI")
graph.create(cad)


vrt_pr_cad=Relationship(vrt,'Est un prérequis à',cad)
graph.create(vrt_pr_cad)

ns_pr_pyn=Relationship(ins,'Est un prérequis à',pyn)
graph.create(ins_pr_pyn)

dns_pr_adns=Relationship(dns,'Est un prérequis à',adns)
graph.create(dns_pr_adns)

isi_pr_sec=Relationship(isi,'Est un prérequis à',sec)
graph.create(isi_pr_sec)

ins_pr_shl=Relationship(ins,'Est un prérequis à',shl)
graph.create(ins_pr_shl)

shl_pr_net=Relationship(shl,'Est un prérequis à',net)
graph.create(shl_pr_net)

net_pr_wan=Relationship(net,'Est un prérequis à',wan)
graph.create(net_pr_wan)

net_pr_ip4=Relationship(net,'Est un prérequis à',ip4)
graph.create(net_pr_ip4)

ip4_pr_ip6=Relationship(ip4,'Est un prérequis à',ip6)
graph.create(ip4_pr_ip6)

ip4_pr_rdyn=Relationship(ip4,'Est un prérequis à',rdyn)
graph.create(ip4_pr_rdyn)

ip6_pr_rdyn=Relationship(ip6,'Est un prérequis à',rdyn)
graph.create(ip6_pr_rdyn)

net_pr_lan=Relationship(net,'Est un prérequis à',lan)
graph.create(net_pr_lan)

lan_pr_wlan=Relationship(lan,'Est un prérequis à',wlan)
graph.create(lan_pr_wlan)

hyp_pr_wlan=Relationship(hyp,'Est un prérequis à',wlan)
graph.create(hyp_pr_wlan)

#shl_pr_hdi=Relationship(shl,'Est un prérequis à',hdi)
#graph.create(shl_pr_hdi)

#hdi_pr_vrt=Relationship(hdi,'Est un prérequis à',vrt)
#graph.create(hdi_pr_vrt)

vdi_pr_tel=Relationship(vdi,'Est un prérequis à',tel)
graph.create(vdi_pr_tel)

ip6_pr_isi=Relationship(ip6,'Est un prérequis à',isi)
graph.create(ip6_pr_isi)


ip6_pr_dir=Relationship(ip6,'Est un prérequis à',dir)
graph.create(ip6_pr_dir)

isi_pr_cry=Relationship(isi,'Est un prérequis à',cry)
graph.create(isi_pr_cry)

cry_pr_tun=Relationship(cry,'Est un prérequis à',tun)
graph.create(cry_pr_tun)

cry_pr_ssh=Relationship(cry,'Est un prérequis à',ssh)
graph.create(cry_pr_ssh)

ip6_pr_dns=Relationship(ip6,'Est un prérequis à',dns)
graph.create(ip6_pr_dns)

ip6_pr_tel=Relationship(ip6,'Est un prérequis à',tel)
graph.create(ip6_pr_tel)

ip6_pr_fwl=Relationship(ip6,'Est un prérequis à',fwl)
graph.create(ip6_pr_fwl)

ip4_pr_fwl=Relationship(ip4,'Est un prérequis à',fwl)
graph.create(ip4_pr_fwl)

ip4_pr_web=Relationship(ip4,'Est un prérequis à',web)
graph.create(ip4_pr_web)

ip6_pr_web=Relationship(ip6,'Est un prérequis à',web)
graph.create(ip6_pr_web)

web_pr_ged=Relationship(web,'Est un prérequis à',ged)
graph.create(web_pr_ged)

fwl_pr_afp=Relationship(fwl,'Est un prérequis à',afp)
graph.create(fwl_pr_afp)

dir_pr_lin=Relationship(dir,'Est un prérequis à',lin)
graph.create(dir_pr_lin)

dir_pr_win=Relationship(dir,'Est un prérequis à',win)
graph.create(dir_pr_win)

win_pr_htr=Relationship(win,'Est un prérequis à',htr)
graph.create(win_pr_htr)
 
dns_pr_win=Relationship(dns,'Est un prérequis à',win)
graph.create(dns_pr_win)

win_pr_dpl=Relationship(win,'Est un prérequis à',dpl)
graph.create(win_pr_dpl)

lin_pr_htr=Relationship(lin,'Est un prérequis à',htr)
graph.create(lin_pr_htr)

lin_pr_dpl=Relationship(lin,'Est un prérequis à',dpl)
graph.create(lin_pr_htr)

dns_pr_lin=Relationship(dns,'Est un prérequis à',lin)
graph.create(dns_pr_lin)

dns_pr_mail=Relationship(dns,'Est un prérequis à',mail)
graph.create(dns_pr_mail)

cry_pr_pgp=Relationship(cry,'Est un prérequis à',pgp)
graph.create(cry_pr_pgp)

mail_pr_pgp=Relationship(mail,'Est un prérequis à',pgp)
graph.create(mail_pr_pgp)

net_pr_cisco=Relationship(net,'Est un prérequis à',cisco)
graph.create(net_pr_cisco)


cry_pr_pki=Relationship(cry,'Est un prérequis à',pki)
graph.create(cry_pr_pki)


