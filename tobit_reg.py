import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy.optimize import minimize
from scipy.stats import norm

class TobitRegression:
    def __init__(self, y, X, lower_bound=0):
        self.y = y
        self.X = X
        self.lb = lower_bound

    def _tobit_log_likelihood(self, params):
        # Extract beta coefficients and sigma
        beta = params[:-1]
        sigma = params[-1]
        if sigma <= 0: return 1e10 # Constraint: sigma must be positive
        
        # Calculate xb (linear predictor)
        xb = np.dot(self.X, beta)
        
        # Binary mask for censored vs uncensored
        cens = (self.y <= self.lb)
        
        # Log-Likelihood for uncensored: LOG(PDF)
        ll_uncens = norm.logpdf(self.y[~cens], loc=xb[~cens], scale=sigma)
        
        # Log-Likelihood for censored: LOG(CDF)
        # Matches CDF('NORMAL', 0, xb, sigma) from your SAS code
        ll_cens = norm.logcdf((self.lb - xb[cens]) / sigma)
        
        return -(np.sum(ll_uncens) + np.sum(ll_cens))

    def fit(self):
        # Initial guesses: b0, b1, b2, sigma
        start_params = np.append(np.zeros(self.X.shape[1]), 1.0)
        res = minimize(self._tobit_log_likelihood, start_params, method='L-BFGS-B')
        self.reg_params = res.x
        return res

