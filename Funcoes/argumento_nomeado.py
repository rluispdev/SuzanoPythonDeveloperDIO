def salvar_carro(marca, modelo, ano, placa):
    print(f"Salvando o carro {marca} {modelo} {ano} {placa}")


salvar_carro("Ford", "Ka", 2010, "ABC-1234")
salvar_carro("Chevrolet", "Celta", 2012, "DEF-5678")    
salvar_carro(ano=2015, placa="GHI-9012", marca="Fiat", modelo="Palio")
salvar_carro(placa="JKL-3456", modelo="Gol", marca="Volkswagen", ano=2018)
salvar_carro("Toyota", "Corolla", placa="MNO-7890", ano=2020)
salvar_carro("Honda", "Civic", 2019, "PQR-1234")
salvar_carro("Hyundai", "HB20", 2017, "STU-5678")

salvar_carro(**{"marca": "Renault", "modelo": "Sandero", "ano": 2016, "placa": "VWX-9012"})
