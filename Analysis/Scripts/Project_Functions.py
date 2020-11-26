import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt



def load_and_process(path_to_csv_file):
    games = (pd.read_csv(path_to_csv_file)
        .drop(columns = ["Game", "Unnamed: 2", "FF", "FA", "FF%", "TOI", "Attendance", "LDSA", "LDSF%", "LDGA", "LDSH%", "LDSV%", "LDCA", "LDCF", "LDCF%", "LDSF", "LDGF", "LDGF%", "MDSA", "MDGA", "MDGF", "MDGF%", "MDSH%", "MDCF%", "MDCA", "MDCF", "MDSF", "MDSV%", "MDSF%", "HDSA", "HDGF", "HDGA", "HDSF", "HDCA", "HDCF"])
         )   
    return games




def group_by(df):
    return games.groupby('Team', as_index = False).mean()




def describe(df):
    return games.describe().T




def CFdata (games):
    CF = (
        games.groupby(
            "Team")["CF%"].mean()
        .reset_index()
        .sort_values(
            by = ["CF%"], ascending = False)
        .reset_index()
        .drop(
            columns = ["index"])
    )
    CF
    fig_dims=(8,6)
    fig, ax = plt.subplots(figsize=fig_dims)
    sns.barplot(x="CF%", y="Team", data = CF, palette = "rocket")
    
    return CF




def PDOdata (games):
    """create a boxplot of PDO by team"""
    PDO = (
        games.groupby(
            "Team")["PDO"].mean()
        .reset_index()
        .sort_values(
            by = ["PDO"], ascending = False)
        .reset_index()
        .drop(
            columns = ["index"])
    )
    PDO
    fig_dims=(8,6)
    fig, ax = plt.subplots(figsize=fig_dims)
    sns.barplot(x="PDO", y="Team", data = PDO, palette = "rocket")
    return PDO





def SVperdata (games):
    """create a boxplot of SV% by team"""
    SV = (
        games.groupby(
            "Team")["SV%"].mean()
        .reset_index()
        .sort_values(
            by = ["SV%"], ascending = False)
        .reset_index()
        .drop(
            columns = ["index"])
    )
    SV
    fig_dims=(8,6)
    fig, ax = plt.subplots(figsize=fig_dims)
    sns.barplot(x="SV%", y="Team", data = SV, palette = "rocket")
    return SV






def SFperdata (df):
    """create a boxplot of SF% by team"""
    SF = (
        df.groupby(
            "Team")["SF%"].mean()
        .reset_index()
        .sort_values(
            by = ["SF%"], ascending = False)
        .reset_index()
        .drop(
            columns = ["index"])
    )
    SF
    fig_dims=(8,6)
    fig, ax = plt.subplots(figsize=fig_dims)
    sns.barplot(x="SF%", y="Team", data = SF, palette = "mako")
    return SF






def xGFdata(df):
    """create a boxplot of xGF% by team"""
    xGF = (
       df.groupby(
            "Team")["xGF%"].mean()
        .reset_index()
        .sort_values(
            by = ["xGF%"], ascending = False)
        .reset_index()
        .drop(
            columns = ["index"])
    )
    xGF
    fig_dims=(8,6)
    fig, ax = plt.subplots(figsize=fig_dims)
    sns.barplot(x="xGF%", y="Team", data = xGF, palette = "mako")
    return xGF




def SFGFdata(df):
   
    SFGF = (
        df.groupby(
            "Team")["SF%","GF%"].mean()
        .reset_index()
        .sort_values(
            by = ["SF%"], ascending = False)
        .reset_index()
        .drop(
            columns = ["index"])
    )
    SFGF
    fig_dims=(12,10)
    fig, ax = plt.subplots(figsize=fig_dims)

    sns.scatterplot(x="SF%", y="GF%", hue="Team", data = SFGF, palette = "tab20")
   
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    return SFGF
