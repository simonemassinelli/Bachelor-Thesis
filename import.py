import os  # To manage file paths and operations
import zipfile  # To work with ZIP files
from datetime import datetime  # To handle and formatting dates
import fnmatch  # To filter file names
import plotly.express as px  # To create interactive charts
import plotly.graph_objects as go  # To add additional shapes to the chart
import pandas as pd  # To handle data in DataFrames
import numpy as np  # To do mathematical and statistical computations
from scipy import signal
from scipy.spatial.distance import mahalanobis # To do the change detection
from astropy.timeseries import LombScargle # To do the spectral analysis
from sklearn.metrics import mean_squared_error # To find trends