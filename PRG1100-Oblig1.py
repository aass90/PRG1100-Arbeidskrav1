#PRG1100-Oblig1-AAA

from tkinter import *


def bil_kalkulator():

    #Utregning av egenkapitalprosent
    egenkapital_prosent=int(egenkapital.get())/int(bil_pris.get())
    nedbet_tid=int(nedbetalingstid.get())
    
    #Sjekker om brukeren har nødvendig egenkapital
    if egenkapital_prosent>0.35:
        if egenkapital_prosent<0.50:
            arlig_rente=0.045
            lanetilsagn.set('Lån innvilges')
            lanetilsagn_1.set('4,5%')
        else:
            if egenkapital_prosent<0.60:
                arlig_rente=0.03
                lanetilsagn.set('Lån innvilges')
                lanetilsagn_1.set('3%')
            else:
                if egenkapital_prosent>=0.60:
                    arlig_rente=0.025
                    lanetilsagn.set('Lån innvilges')
                    lanetilsagn_1.set('2,5%')
                else:
                    lanetilsagn.set('Du trenger ikke lån')
                    lanetilsagn_1.set('0%')

        #Om egenkapital er godkjent går vi videre til avsluttende del som angår terminbeløp
        egenkapital_prosent=int(bil_pris.get())-int(egenkapital.get())
        lanebelop.set(format(egenkapital_prosent,'.0f'))

        term_rente=(arlig_rente/12)
        terminrente_prosent.set(format(term_rente*100,'.2f'))

        ant_terminer=(nedbet_tid*12)
        antall_terminer.set(ant_terminer)

        terminbelop_res=egenkapital_prosent*(((1+term_rente)**ant_terminer)*term_rente/(((1+term_rente)**ant_terminer)-1))
        terminbelop.set(format(terminbelop_res,'.0f'))

    else:
        lanetilsagn.set('Lån kan ikke innvilges')
        

window=Tk()

#Navngir vindu
window.title('Lånekalkulator billån')

#Ledetekster
lbl_sum_bil=Label(window, text='Bilpris:', font='Helvetica 10 bold')
lbl_sum_bil.grid(row=0, column=0, padx=5, pady=10, sticky=E)

lbl_egenkap=Label(window, text='Egenkapital:', font='Helvetica 10 bold')
lbl_egenkap.grid(row=1, column=0, padx=5, pady=10, sticky=E)

lbl_nedbetaling=Label(window, text='Nedbetalingstid:', font='Helvetica 10 bold')
lbl_nedbetaling.grid(row=2, column=0, padx=5, pady=10, sticky=E)

lbl_lanetilsagn=Label(window, text='Lånetilsagn:', font='Helvetica 10 bold')
lbl_lanetilsagn.grid(row=4, column=1, padx=5, pady=10, sticky=S)

lbl_rente_ar=Label(window, text='Årlig rente:', font='Helvetica 10 bold')
lbl_rente_ar.grid(row=8, column=0, padx=5, pady=10, sticky=E)

lbl_tot_lan=Label(window, text='Lånebeløp:', font='Helvetica 10 bold')
lbl_tot_lan.grid(row=6, column=0, padx=5, pady=10, sticky=E)

lbl_term_rente=Label(window, text='Terminrente:', font='Helvetica 10 bold')
lbl_term_rente.grid(row=9, column=0, padx=5, pady=10, sticky=E)

lbl_ant_term=Label(window, text='Antall terminer:', font='Helvetica 10 bold')
lbl_ant_term.grid(row=10, column=0, padx=5, pady=10, sticky=E)

lbl_term_belop=Label(window, text='Terminbeløp:', font='Helvetica 10 bold')
lbl_term_belop.grid(row=7, column=0, padx=5, pady=10, sticky=E)

#Inndata
bil_pris=StringVar()
ent_bil_pris=Entry(window, width=9, textvariable=bil_pris)
ent_bil_pris.grid(row=0, column=2, padx=5, pady=10, sticky=W)

egenkapital=StringVar()
ent_egenkap=Entry(window, width=9, textvariable=egenkapital)
ent_egenkap.grid(row=1, column=2, padx=5, pady=10, sticky=W)

nedbetalingstid=StringVar()
ent_nedbetaling=Entry(window, width=4, textvariable=nedbetalingstid)
ent_nedbetaling.grid(row=2, column=2, padx=5, pady=10, sticky=W)

#Utdata
lanetilsagn=StringVar()
ent_lanetilsagn=Entry(window, width=20, state='readonly', textvariable=lanetilsagn)
ent_lanetilsagn.grid(row=5, column=1, padx=10, pady=15, sticky=W)

lanetilsagn_1=StringVar()
ent_rente_ar=Entry(window, width=5, state='readonly', textvariable=lanetilsagn_1)
ent_rente_ar.grid(row=8, column=2, padx=10, pady=15, sticky=W)

lanebelop=StringVar()
ent_lanebelop=Entry(window, width=10, state='readonly', textvariable=lanebelop)
ent_lanebelop.grid(row=6, column=2, padx=10, pady=15, sticky=W)

terminrente_prosent=StringVar()
ent_term_rente=Entry(window, width=5, state='readonly', textvariable=terminrente_prosent)
ent_term_rente.grid(row=9, column=2, padx=10, pady=15, sticky=W)

antall_terminer=StringVar()
ent_ant_term=Entry(window, width=5, state='readonly', textvariable=antall_terminer)
ent_ant_term.grid(row=10, column=2, padx=10, pady=15, sticky=W)

terminbelop=StringVar()
ent_term_belop=Entry(window, width=8, state='readonly', textvariable=terminbelop)
ent_term_belop.grid(row=7, column=2, padx=10, pady=15, sticky=W)

#Knapper
btn_beregn=Button(window, text='Beregn lån:', font='Helvetica 10 bold', bg='blue', command=bil_kalkulator)
btn_beregn.grid(row=3, column=1, padx=10, pady=15, sticky=S)

btn_avslutt=Button(window, text='Avslutt', font='Helvetica 10 bold', bg='red', command=window.destroy)
btn_avslutt.grid(row=11, column=3, pady=15, sticky=W)



window.mainloop()
