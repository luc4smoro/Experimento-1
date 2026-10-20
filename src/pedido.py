def calcular_total_pedido(subtotal, distancia_km, cliente_vip=False):
    """Calcula o valor final de um pedido.

    A implementação inicial contém defeitos e deve ser corrigida
    de acordo com os requisitos descritos no README.
    """

    if subtotal < 0 or distancia_km < 0:
        raise ValueError("Subtotal e distância não podem ser negativos")

    desconto = 10 

    subtotal_final = subtotal

    frete = 0
    
    if(cliente_vip):
        subtotal_final = subtotal - ((subtotal * 10) / 100)

    if(cliente_vip and subtotal_final >= 100):
        frete = 0
    else:
        frete = 8 + (1.5 * distancia_km)

    final_total = subtotal_final + frete
    return float(final_total)
    

    # subtotal_com_desconto = subtotal - desconto

    # if subtotal_com_desconto > 100:
    #     frete = 0
    # else:
    #     frete = 8 + distancia_km

    # total = subtotal + frete
    # return total
