# -*- coding: UTF-8 -*-

from vertex import Vertex
from adjacent import Adjacent


class Graph:
    portoUniao = Vertex('Porto União', 203)
    pauloFrontin = Vertex('Paulo Frontin', 172)
    canoinhas = Vertex('Canoinhas', 141)
    irati = Vertex('Irati', 139)
    palmeira = Vertex('Palmeira', 59)
    campoLargo = Vertex('Campo Largo', 27)
    curitiba = Vertex('Curitiba', 0)
    balsaNova = Vertex('Balsa Nova', 41)
    araucaria = Vertex('Araucária', 23)
    saoJose = Vertex('São José dos Pinhais', 13)
    contenda = Vertex('Contenda', 39)
    mafra = Vertex('Mafra', 94)
    tijucas = Vertex('Tijucas do Sul', 56)
    lapa = Vertex('Lapa', 74)
    saoMateus = Vertex('São Mateus do Sul', 123)
    tresBarras = Vertex('Três Barras', 131)

    portoUniao.add_adjacent(Adjacent(pauloFrontin, 46))
    portoUniao.add_adjacent(Adjacent(canoinhas, 78))
    portoUniao.add_adjacent(Adjacent(saoMateus, 87))

    pauloFrontin.add_adjacent(Adjacent(portoUniao, 46))
    pauloFrontin.add_adjacent(Adjacent(irati, 75))

    canoinhas.add_adjacent(Adjacent(portoUniao, 78))
    canoinhas.add_adjacent(Adjacent(tresBarras, 12))
    canoinhas.add_adjacent(Adjacent(mafra, 66))

    irati.add_adjacent(Adjacent(pauloFrontin, 75))
    irati.add_adjacent(Adjacent(palmeira, 75))
    irati.add_adjacent(Adjacent(saoMateus, 57))

    palmeira.add_adjacent(Adjacent(irati, 75))
    palmeira.add_adjacent(Adjacent(saoMateus, 77))
    palmeira.add_adjacent(Adjacent(campoLargo, 55))

    campoLargo.add_adjacent(Adjacent(palmeira, 55))
    campoLargo.add_adjacent(Adjacent(balsaNova, 22))
    campoLargo.add_adjacent(Adjacent(curitiba, 29))

    curitiba.add_adjacent(Adjacent(campoLargo, 29))
    curitiba.add_adjacent(Adjacent(balsaNova, 51))
    curitiba.add_adjacent(Adjacent(araucaria, 37))
    curitiba.add_adjacent(Adjacent(saoJose, 15))

    balsaNova.add_adjacent(Adjacent(curitiba, 51))
    balsaNova.add_adjacent(Adjacent(campoLargo, 22))
    balsaNova.add_adjacent(Adjacent(contenda, 19))

    araucaria.add_adjacent(Adjacent(curitiba, 37))
    araucaria.add_adjacent(Adjacent(contenda, 18))

    saoJose.add_adjacent(Adjacent(curitiba, 15))
    saoJose.add_adjacent(Adjacent(tijucas, 49))

    contenda.add_adjacent(Adjacent(balsaNova, 19))
    contenda.add_adjacent(Adjacent(araucaria, 18))
    contenda.add_adjacent(Adjacent(lapa, 26))

    mafra.add_adjacent(Adjacent(tijucas, 99))
    mafra.add_adjacent(Adjacent(lapa, 57))
    mafra.add_adjacent(Adjacent(canoinhas, 66))

    tijucas.add_adjacent(Adjacent(mafra, 99))
    tijucas.add_adjacent(Adjacent(saoJose, 49))

    lapa.add_adjacent(Adjacent(contenda, 26))
    lapa.add_adjacent(Adjacent(saoMateus, 60))
    lapa.add_adjacent(Adjacent(mafra, 57))

    saoMateus.add_adjacent(Adjacent(palmeira, 77))
    saoMateus.add_adjacent(Adjacent(irati, 57))
    saoMateus.add_adjacent(Adjacent(lapa, 60))
    saoMateus.add_adjacent(Adjacent(tresBarras, 43))
    saoMateus.add_adjacent(Adjacent(portoUniao, 87))

    tresBarras.add_adjacent(Adjacent(saoMateus, 43))
    tresBarras.add_adjacent(Adjacent(canoinhas, 12))
