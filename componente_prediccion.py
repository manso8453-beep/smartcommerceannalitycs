#componente matematico aislado o independiente q realiza calculos de estimacion del inventario futuro.
import pandas as pd
import numpy as np

#creamos la clase principal del motor de prediccion.
class MotorPrediccion:
    #componente analitico para estimar la demanda futura del inventario.
    def __init__(self, incremento_simulado = 0.15
                 ):
        self.incremento = incremento_simulado
    
    def predecir_demanda(self, df_historico: pd.DataFrame) -> pd.DataFrame:
        """
        toma datos historicos y estima stock necesario para el proximo mes.
        Logica del componente aislada del UI.
        """
        if df_historico.empty:
            return pd.DataFrame()
        
        #agrupamos por producto para ver promedio ventas mensuales
        ventas_promedio = df_historico.groupby("producto")['cantidad'].mean().reset_index()

        #aplicamos la formula matematica del stock sugerido (Demanda + Margen de seguridad)
        ventas_promedio['stock_sugerido'] = np.ceil(ventas_promedio['cantidad'] * (1 + self.incremento)).astype(int)
        ventas_promedio.rename(columns={'cantidad': 'promedio_historico'}, inplace=True)
        return ventas_promedio 
    

        