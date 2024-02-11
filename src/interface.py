import tkinter as tk
from tkinter import ttk,simpledialog

from src.components.tab import Tab



def transform_table():
    # Logique pour transformer la table
    print("Transformer la table")


# Fonction bouton sauvegarde de la table
def save_table(tab):
    def save(tab):
        path = entry_path.get()
        filename = entry_filename.get()
        file_type = variable_type.get()
    
        if path and filename and file_type:
            result_string = f"{path}/{filename}.{file_type}"
            print(result_string)
            tab.save(filename,path,file_type)
            root.destroy()
        else:
            print("Veuillez remplir tous les champs.")
    
    # Creation fenetre
    root = tk.Tk()
    root.title("Save table")
    
    # les champs d entrées
    label_path = ttk.Label(root, text="Path:")
    entry_path = ttk.Entry(root)
    
    label_filename = ttk.Label(root, text="File name:")
    entry_filename = ttk.Entry(root)
    
    # label_type = ttk.Label(root, text="Type:")
    # entry_type = ttk.Entry(root)

    # Menu déroulant type
    type = ["","csv","json"]
    
    variable_type = tk.StringVar(root)
    label_type = ttk.Label(root, text="Type:")
    menu_type = ttk.OptionMenu(root, variable_type, *type)
    
    
    # Bouton save
    button_save = ttk.Button(root, text="Save", command=lambda : save(tab))
    
    # Grille de bouton
    label_path.grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_path.grid(row=0, column=1, padx=10, pady=5)
    
    label_filename.grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_filename.grid(row=1, column=1, padx=10, pady=5)
    
    label_type.grid(row=2, column=0, padx=10, pady=5, sticky="e")
    menu_type.grid(row=2, column=1, padx=10, pady=5)
    
    button_save.grid(row=3, column=0, columnspan=2, pady=10)
    

    root.mainloop()



# Fonction bouton load new table de la table
def load_table(c_tab=None):

    #New tab
    tab = Tab()
    
    #List of modifications
    modifications = [tab]
    
    if(c_tab is None):
        user_input = simpledialog.askstring("Load new table", "Enter your file path :")
        
        if user_input is not None:
            # Chargemant de Tab
            tab.load(user_input)
    else:
        tab = c_tab

    #tab copy
    original_tab = tab
    

    root = tk.Tk()
    root.title(tab.file_path)

    def reset(tab):
        modifications.append(tab)
        
        for item in tree.get_children():
            tree.delete(item)

        for item in original_tab.data:
            values = [item[col] for col in columns]
            tree.insert("", "end", values=values)
            
        tab = original_tab

    # Fonction bouton filter de la table
    def filter_table(tab):
        # def reset(tab):
        #     for item in tree.get_children():
        #         tree.delete(item)

        #     for item in tab.data:
        #         values = [item[col] for col in columns]
        #         tree.insert("", "end", values=values)            
            
        def apply_filter(tab):
            # modifications.append(tab)
            
            for item in tree.get_children():
                tree.delete(item)
            
            column = variable_column.get()
            rel = variable_filter.get()
            value = variable_value.get()      


            if(rel=="IS EQUAL" and str in tab.columns_type[column]):
                print("HERE")
                filter_tab = tab.filter(column=column,rel=rel,value=value)
                # filter_tab.show()
            else:
                filter_tab = tab.filter(column=column,rel=rel,value=int(value))
            # root.destroy()
            # load_table(c_tab = filter_tab)
            for item in filter_tab.data:
                values = [item[col] for col in columns]
                tree.insert("", "end", values=values)
            # tab = filter_tab
    
        root = tk.Tk()
        root.title("Filter")
        
        
        # variables
        variable_column = tk.StringVar(root)
        variable_filter = tk.StringVar(root)
        variable_value = tk.StringVar(root)
        
    
        # Menu déroulant colonnes
        label_column = ttk.Label(root, text="Column")
        tmp = [""]+tab.columns
        menu_column = ttk.OptionMenu(root, variable_column, *tmp)
    
    
        label_column.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        menu_column.grid(row=0, column=1, padx=10, pady=5)
        
        # Menu déroulant filtres
        filters = ["","IS EQUAL","IS GREATER THAN","IS GREATER THAN OR EQUAL","IS LESS THAN","IS LESS THAN OR EQUAL"]
        
        label_filter = ttk.Label(root, text="Filter:")
        menu_filter = ttk.OptionMenu(root, variable_filter, *filters)
        label_filter.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        menu_filter.grid(row=1, column=1, padx=10, pady=5)
        
        # value
        label_value = ttk.Label(root, text="Value:")
        variable_value = ttk.Entry(root)
        label_value.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        variable_value.grid(row=2, column=1, padx=10, pady=5)
        
        # Bouton filter
        button_filter = ttk.Button(root, text="Filter", command=lambda : apply_filter(tab))
        button_filter.grid(row=3, column=0, columnspan=2, pady=10)


        # # Bouton reset
        # button_reset = ttk.Button(root, text="Reset", command=lambda : reset(tab))
        # button_reset.grid(row=3, column=2, columnspan=2, pady=10)
        # root.mainloop()

    

    def sort_table(tab):

        # Effacer le tableau (tree)
        user_input = simpledialog.askstring("Sort table", "On :")
        
        for item in tree.get_children():
            tree.delete(item)

        sorted_tab = tab.sort(column=user_input,reverse=False)
        sorted_tab.show()
        
        for item in sorted_tab.data:
            values = [item[col] for col in columns]
            tree.insert("", "end", values=values)

        
    button_load = ttk.Button(root, text="Load new table", command=load_table)
    button_transform = ttk.Button(root, text="Transform table", command=transform_table)
    button_filter = ttk.Button(root, text="Filter", command=lambda : filter_table(tab))
    button_save = ttk.Button(root, text="Save table", command=lambda: save_table(tab))
    button_sort_table = ttk.Button(root, text="Sort Table", command=lambda: sort_table(tab))
    button_reset = ttk.Button(root, text="Reset", command=lambda : reset(tab))
        

    button_load.grid(row=0, column=1)
    button_transform.grid(row=0, column=2)
    button_filter.grid(row=0, column=3)
    button_sort_table.grid(row=0, column = 4)
    button_reset.grid(row=0,column=5)
    button_save.grid(row=0, column=6)
    
    # Treeview pour faire des tableaux
    tree = ttk.Treeview(root)
        
    # scroll barre
    horizontal_scrollbar = ttk.Scrollbar(root, orient="horizontal", command=tree.xview)
    tree.configure(xscrollcommand=horizontal_scrollbar.set)
        
        
    # les colonnes
    columns = tab.columns
    tree["columns"] = columns
        
    for col in columns:
        tree.column(col, anchor="center")
        tree.heading(col, text=col, anchor="center")
        
    # les lignes
    for item in tab.data:
        values = [item[col] for col in columns]
        tree.insert("", "end", values=values)
        
    # treeview config
    tree.grid(row=1, column=0, columnspan=10, padx=10, pady=10, sticky="nsew")
    horizontal_scrollbar.grid(row=2, column=0, columnspan=4, sticky="ew")
    
    
    
    # truc de redimenssionnement
    root.columnconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
        

    root.mainloop()


# lancement de l'interface
def launch():
    root = tk.Tk()
    root.geometry("400x400")
    root.title("Data Filter")
    root.resizable(height=True,width=True)
    
    title_label = ttk.Label(root, text="Data Filter", font=("Helvetica", 16, "bold"))
    title_label.pack(pady=5)
    
    button = ttk.Button(root, text="Load table", command=load_table)
    button.pack(padx=10, pady=10)


    root.mainloop()