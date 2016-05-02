import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
BASE = declarative_base()

class DatosGenerales(BASE):
    __tablename__ = 't501'
    id = Column(Integer, primary_key=True)
    patente_aduanal = Column(String(4))
    indice = Column(String(7))
    clave_de_seccion_aduanera_de_despacho = Column(String(3))
    clave_de_tipo_de_operacion = Column(String(1))
    clave_de_documento = Column(String(3))
    clave_de_aduana_de_entrada = Column(String(3))
    tipo_de_cambio = Column(Float())
    total_de_fletes = Column(Float())
    total_de_seguros = Column(Float())
    total_de_embalajes = Column(Float())
    total_de_otros_incrementables = Column(Float())
    total_de_otros_deducibles = Column(Float())
    peso_bruto_de_la_mercancia = Column(Float())
    clave_de_medio_de_transporte_de_salida = Column(Integer())
    clave_de_medio_de_transporte_de_arribo = Column(Integer())
    clave_de_medio_de_transporte_de_entrada_o_salida = Column(Integer())
    clave_de_destino_de_la_mercancia = Column(Integer())
    fecha_de_balanza = Column(String(1))
    clave_de_tipo_de_pedimento = Column(String(1))
    bandera_de_despacho = Column(Date())
    fecha_de_pago_real = Column(Date())
    '''
    transporte_de_las_mercancias = relationship('TransporteDeLasMercancias')
    guias = relationship('Guias')
    contenedores =  relationship('Contenedores')
    facturas = relationship('Facturas')
    fechas_del_pedimento = relationship('FechasDelPedimento')
    casos_del_pedimento = relationship('CasosDelPedimento')
    tasas_de_pedimento = relationship('TasasDePedimento')
    contribuciones_del_pedimento = relationship('ContribucionesDelPedimento')
    descargos_de_mercancias = relationship('DescargosDeMercancias')
    destinatarios_de_la_mercancia = relationship('DestinatariosDeLaMercancia')
    partidas = relationship('Partidas')
    '''
class TransporteDeLasMercancias(BASE):
    __tablename__ = 't502'
    id = Column(Integer, primary_key=True)
    datos_generales_id = Column(Integer, ForeignKey('t501.id'))
    t501 = relationship('DatosGenerales')
    #patente_aduanal = Column(String(4))
    #indice = Column(String(7))
    #clave_de_seccion_aduanera_de_despacho = Column(String(3))
    clave_de_pais_de_transporte = Column(String(3))
    fecha_de_balanza = Column(Date())
    fecha_de_pago_real = Column(Date())

class Guias(BASE):
    __tablename__ = 't503'
    id = Column(Integer, primary_key=True)
    t501_id = Column(Integer, ForeignKey('t501.id'))
    t501 = relationship('DatosGenerales')
    #patente_aduanal = Column(String(4))
    #indice = Column(String(7))
    #clave_de_seccion_aduanera_de_despacho = Column(String(3))
    clave_de_tipo_de_guia = Column(String(3))
    fecha_de_balanza = Column(Date())
    fecha_de_pago_real = Column(Date())
class Contenedores(BASE):
    __tablename__ = 't504'
    id = Column(Integer, primary_key=True)
    t501_id = Column(Integer, ForeignKey('t501.id'))
    t501 = relationship('DatosGenerales')
    #patente_aduanal = Column(String(4))
    #indice = Column(String(7))
    #clave_de_seccion_aduanera_de_despacho = Column(String(3))
    clave_de_tipo_de_contenedor = Column(String(2))
    fecha_de_balanza = Column(Date())
    fecha_de_pago_real = Column(Date())
class Facturas(BASE):
    __tablename__ = 't505'
    id = Column(Integer, primary_key=True)
    t501_id = Column(Integer, ForeignKey('t501.id'))
    t501 = relationship('DatosGenerales')
    #patente_aduanal = Column(String(4))
    #indice = Column(String(7))
    #clave_de_seccion_aduanera_de_despacho = Column(String(3))
    fecha_de_facturacion = Column(Date())
    clave_de_termino_de_la_facturacion = Column(String(3))
    clave_de_moneda_de_facturacion = Column(String(3))
    valor_en_dolares = Column(Float())
    valor_en_moneda_extranjera = Column(Float())
    clave_de_pais_de_facturacion = Column(String(3))
    clave_de_entidad_federativa_de_la_facturacion = Column(String(3))
    fecha_de_balanza = Column(Date())
    fecha_de_pago_real = Column(Date())
class FechasDelPedimento(BASE):
    __tablename__ = 't506'
    id = Column(Integer, primary_key=True)
    t501_id = Column(Integer, ForeignKey('t501.id'))
    t501 = relationship('DatosGenerales')
    #patente_aduanal = Column(String(4))
    #indice = Column(String(7))
    #clave_de_seccion_aduanera_de_despacho = Column(String(3))
    clave_de_tipo_de_fecha = Column(Integer())
    fecha_de_operacion = Column(Float())
    fecha_de_balanza = Column(Date())
    fecha_de_pago_real = Column(Date())
class CasosDelPedimento(BASE):
    __tablename__ = 't507'
    id = Column(Integer, primary_key=True)
    t501_id = Column(Integer, ForeignKey('t501.id'))
    t501 = relationship('DatosGenerales')
    #patente_aduanal = Column(String(4))
    #indice = Column(String(7))
    #clave_de_seccion_aduanera_de_despacho = Column(String(3))
    clave_de_caso = Column(String(2))
    identificador_de_caso = Column(String(20))
    fecha_de_balanza = Column(Date())
    fecha_de_pago_real = Column(Date())
class TasasDePedimento(BASE):
    __tablename__ = 't509'
    id = Column(Integer, primary_key=True)
    t501_id = Column(Integer, ForeignKey('t501.id'))
    t501 = relationship('DatosGenerales')
    #patente_aduanal = Column(String(4))
    #indice = Column(String(7))
    #clave_de_seccion_aduanera_de_despacho = Column(String(3))
    clave_de_contribucion = Column(Integer())
    tasa_de_contribucion = Column(Float())
    clave_de_tipo_de_tasa = Column(Integer())
    fecha_de_balanza = Column(Date())
    fecha_de_pago_real = Column(Date())
class ContribucionesDelPedimento(BASE):
    __tablename__ = 't510'
    id = Column(Integer, primary_key=True)
    t501_id = Column(Integer, ForeignKey('t501.id'))
    t501 = relationship('DatosGenerales')
    #patente_aduanal = Column(String(4))
    #indice = Column(String(7))
    #clave_de_seccion_aduanera_de_despacho = Column(String(3))
    clave_de_contribucion = Column(Integer())
    clave_de_forma_de_pago = Column(Integer())
    importe_del_pago = Column(Float)
    fecha_de_balanza = Column(Date())
    fecha_de_pago_real = Column(Date())
class DescargosDeMercancias(BASE):
    __tablename__ = 't512'
    id = Column(Integer, primary_key=True)
    t501_id = Column(Integer, ForeignKey('t501.id'))
    t501 = relationship('DatosGenerales')
    #patente_aduanal = Column(String(4))
    #indice = Column(String(7))
    #clave_de_seccion_aduanera_de_despacho = Column(String(3))
    patente_aduanal_original = Column(String(4))
    indice_original = Column(String(7))
    clave_de_seccion_aduanera_de_despacho_original = Column(String(3))
    clave_de_documento_original = Column(String(3))
    fecha_de_la_operacion_original = Column(Date())
    fraccion_arancelaria_original = Column(String(8))
    clave_de_unidad_de_medida_original = Column(Integer())
    cantidad_de_mercancia_descargada = Column(Float())
    fecha_de_balanza = Column(Date())
    fecha_de_pago_real = Column(Date())
class DestinatariosDeLaMercancia(BASE):
    __tablename__ = 't520'
    id = Column(Integer, primary_key=True)
    t501_id = Column(Integer, ForeignKey('t501.id'))
    t501 = relationship('DatosGenerales')
    #patente_aduanal = Column(String(4))
    #indice = Column(String(7))
    #clave_de_seccion_aduanera_de_despacho = Column(String(3))
    clave_del_pais_del_domicilio_del_destinatario = Column(String(3))
    fecha_de_balanza = Column(Date())
    fecha_de_pago_real = Column(Date())
class Partidas(BASE):
    __tablename__ = 't551'
    id = Column(Integer, primary_key=True)
    t501_id = Column(Integer, ForeignKey('t501.id'))
    t501 = relationship('DatosGenerales')
    #patente_aduanal = Column(String(4))
    #indice = Column(String(7))
    #clave_de_seccion_aduanera_de_despacho = Column(String(3))
    fraccion_arancelaria = Column(String(8))
    secuencia_de_fraccion_arancelaria = Column(Integer())
    subdivision_de_la_fraccion_arancelaria = Column(String(3))
    descripcion_de_la_mercancia = Column(String(250))
    precio_unitario = Column(Float())
    valor_en_aduana = Column(Float())
    valor_comercial = Column(Float())
    valor_en_dolares = Column(Float())
    cantidad_de_mercacionas_en_unidades_de_medida_comercial = Column(Float())
    clave_de_unidad_de_medida_comercial = Column(Integer())
    cantidad_de_mercancia_en_unidades_de_medida_de_la_tarifa = Column(Float())
    clave_de_unidad_de_medida_de_la_tarifa = Column(Integer())
    valor_agregado = Column(Float())
    clave_de_vinculacion = Column(Integer())
    clave_de_metodo_de_valorizacion = Column(Integer())
    codigo_de_la_mercancia_o_producto = Column(String(20))
    marca_de_la_mercancia_o_producto = Column(String(80))
    modelo_de_la_mercancia_o_producto = Column(String(80))
    clave_de_pais_origen_destino = Column(String(3))
    clave_de_pais_comprador_vendedor = Column(String(3))
    clave_de_entidad_federativa_de_origen = Column(String(3))
    clave_de_entidad_federativa_de_destino = Column(String(3))
    clave_de_entidad_federativa_de_comprador = Column(String(3))
    clave_de_entidad_federativa_de_vendedor = Column(String(3))
    fecha_de_balanza = Column(Date())
    fecha_de_pago_real = Column(Date())
    '''
    mercancias = relationship('Mercancias')
    permisos_de_la_partida = relationship('PermisosDeLaPartida')
    casos_de_la_partida = relationship('CasosDeLaPartida')
    tasas_de_las_contribuciones_de_la_partida = relationship('TasasDeLasContribucionesDeLaPartida')
    contribuciones_de_la_partida = relationship('ContribucionesDeLaPartida')
    '''
class Mercancias(BASE):
    __tablename__ = 't552'
    id = Column(Integer, primary_key=True)
    partidas_id = Column(Integer, ForeignKey('t551.id'))
    t551 = relationship('t551')
    #patente_aduanal = Column(String(4))
    #indice = Column(String(7))
    #clave_de_seccion_aduanera_de_despacho = Column(String(3))
    #fraccion_arancelaria = Column(String(8))
    secuencia_de_fraccion_arancelaria = Column(Integer())
    kilometraje_del_vehiculo = Column(Integer())
    fecha_de_balanza = Column(Date())
    fecha_de_pago_real = Column(Date())
class PermisosDeLaPartida(BASE):
    __tablename__ = 't553'
    id = Column(Integer, primary_key=True)
    t551_id = Column(Integer, ForeignKey('t551.id'))
    t551 = relationship('t551')
    #patente_aduanal = Column(String(4))
    #indice = Column(String(7))
    #clave_de_seccion_aduanera_de_despacho = Column(String(3))
    #fraccion_arancelaria = Column(String(8))
    secuencia_de_fraccion_arancelaria = Column(Integer())
    clave_de_permiso = Column(String(2))
    valor_comercial_en_dolares = Column(Float())
    cantidad_de_mercacia_en_unidades_de_la_medida_de_la_tarifa = Column(Float())
    fecha_de_balanza = Column(Date())
    fecha_de_pago_real = Column(Date())
class CasosDeLaPartida(BASE):
    __tablename__ = 't554'
    id = Column(Integer, primary_key=True)
    t551_id = Column(Integer, ForeignKey('t551.id'))
    t551 = relationship('t551')
    #patente_aduanal = Column(String(4))
    #indice = Column(String(7))
    #clave_de_seccion_aduanera_de_despacho = Column(String(3))
    #fraccion_arancelaria = Column(String(8))
    secuencia_de_fraccion_arancelaria = Column(Integer())
    clave_de_caso = Column(String(2))
    identificador_del_caso = Column(String(20))
    fecha_de_balanza = Column(Date())
    fecha_de_pago_real = Column(Date())
class TasasDeLasContribucionesDeLaPartida(BASE):
    __tablename__ = 't556'
    id = Column(Integer, primary_key=True)
    t551_id = Column(Integer, ForeignKey('t551.id'))
    t551 = relationship('t551')
    #patente_aduanal = Column(String(4))
    #indice = Column(String(7))
    #clave_de_seccion_aduanera_de_despacho = Column(String(3))
    #fraccion_arancelaria = Column(String(8))
    secuencia_de_fraccion_arancelaria = Column(Integer())
    clave_de_contribucion = Column(Integer())
    tasa_de_la_contribucion = Column(Float())
    clave_de_tipo_de_la_tasa = Column(Integer())
    fecha_de_balanza = Column(Date())
    fecha_de_pago_real = Column(Date())
class ContribucionesDeLaPartida(BASE):
    __tablename__ = 't557'
    id = Column(Integer, primary_key=True)
    t551_id = Column(Integer, ForeignKey('t551.id'))
    t551 = relationship('t551')
    #patente_aduanal = Column(String(4))
    #indice = Column(String(7))
    #clave_de_seccion_aduanera_de_despacho = Column(String(3))
    #fraccion_arancelaria = Column(String(8))
    secuencia_de_fraccion_arancelaria = Column(Integer())
    clave_de_contribucion = Column(Integer())
    clave_de_forma_de_pago = Column(Integer())
    importe_de_pago = Column(Float())
    fecha_de_balanza = Column(Date())
    fecha_de_pago_real = Column(Date())

ENGINE = create_engine('sqlite:///dpa.db')
BASE.metadata.drop_all(ENGINE)
BASE.metadata.create_all(ENGINE)