(function() {
  /**
   * PxLocalizeBehavior extends app-localize-behavior and provides localization for all Predix UI components.
   *
   * @polymerBehavior PxLocalizeBehavior
   */
  var PxLocalizeBehaviorImpl = {

    properties: {

      language: {
        type: String,
        value: 'en'
      },

      useKeyIfMissing: {
        type: Boolean,
        value: true
      },

      resources: {
        type: Object,
        value: function() {
          return {
            // German
            "de": {
              "Apply": "Übernehmen",
              "Cancel": "Abbrechen",
              "Choose File": "Datei wählen",
              "Clockwise": "Im Uhrzeigersinn",
              "Counter clockwise": "Gegen den Uhrzeigersinn",
              "Date": "Datum",
              "Filter": "Filter",
              "Invalid file type.": "Ungültiger Dateityp",
              "Max": "Max",
              "Min": "Min",
              "Name": "Name",
              "No file selected": "Keine Datei ausgewählt",
              "of": "aus",
              "OK": "OK",
              "Only one file is allowed.": "Es ist nur eine Datei erlaubt.",
              "Open": "Öffnen",
              "Presets": "Voreinstellungen",
              "Reset Zoom": "Zoom zurücksetzen",
              "Rows per page": "Zeilen pro Seite",
              "Severity": "Schwere",
              "Show Less": "Zeige weniger",
              "Show More": "Zeige mehr",
              "Show/Hide Column": "Spalte zeigen / Spalte verstecken",
              "Sign In": "Einloggen",
              "Sign Out": "Ausloggen",
              "Size": "Dateigröße",
              "Sort": "Sortieren",
              "Subtitle": "Untertitel",
              "Title": "Titel",
              "TO": "AN",
              "Total": "Summe",
              "Type": "Art",
              "Zoom in": "Hineinzoomen",
              "Zoom out": "Rauszoomen"
            },
            // English
            "en": {
              "Apply": "Apply",
              "Cancel": "Cancel",
              "Choose File": "Choose File",
              "Clockwise": "Clockwise",
              "Counter clockwise": "Counter clockwise",
              "Date": "Date",
              "Filter": "Filter",
              "Invalid file type.": "Invalid file type.",
              "Max": "Max",
              "Min": "Min",
              "Name": "Name",
              "No file selected": "No file selected",
              "of": "of",
              "OK": "OK",
              "Only one file is allowed.": "Only one file is allowed.",
              "Open": "Open",
              "Presets": "Presets",
              "Reset Zoom": "Reset Zoom",
              "Rows per page": "Rows per page",
              "Severity": "Severity",
              "Show/Hide Column": "Show/Hide Column",
              "Show Less": "Show Less",
              "Show More": "Show More",
              "Sign In": "Sign In",
              "Sign Out": "Sign Out",
              "Size": "Size",
              "Subtitle": "Subtitle",
              "Sort": "Sort",
              "Title": "Title",
              "TO": "TO",
              "Total": "Total",
              "Type": "Type",
              "Zoom in": "Zoom in",
              "Zoom out": "Zoom out"
            },

            // Spanish
            "es": {
              "Apply": "Aplicar",
              "Cancel": "Cancelar",
              "Choose File": "Elija el archivo",
              "Clockwise": "Sentido del reloj",
              "Counter clockwise": "Contra de las manecillas del reloj",
              "Date": "Fecha",
              "Filter": "Filtro",
              "Invalid file type.": "Tipo de archivo invalido.",
              "Max": "Máx",
              "Min": "Mín",
              "Name": "Nombre",
              "No file selected": "Ningún archivo seleccionado",
              "of": "de",
              "OK": "OK",
              "Only one file is allowed.": "Sólo se permite un archivo.",
              "Open": "Abrir",
              "Presets": "Programas",
              "Reset Zoom": "Restablecer Zoom",
              "Rows per page": "Filas por página",
              "Severity": "Severidad",
              "Show/Hide Column": "Mostrar/Esconder Columna",
              "Show Less": "Mostrar menos",
              "Show More": "Mostrar más",
              "Sign In": "Iniciar Sesión",
              "Sign Out": "Cerrar Sesión",
              "Size": "Tamaño",
              "Subtitle": "Subtitulo",
              "Sort": "Ordenar",
              "Title": "Título",
              "TO": "A",
              "Total": "Total",
              "Type": "Tipo",
              "Zoom in": "Acercarse",
              "Zoom out": "Disminuir el zoom"
            },

            // French
            "fr": {
              "Apply": "Appliquer",
              "Cancel": "Annuler",
              "Choose File": "Choisir le fichier",
              "Clockwise": "Sens horaire",
              "Counter clockwise": "Sens antihoraire",
              "Date": "Date",
              "Filter": "Filtre",
              "Invalid file type.": "Type de fichier invalide",
              "Max": "Max",
              "Min": "Min",
              "Name": "Prénom",
              "No file selected": "Aucun fichier sélectionné",
              "of": "de",
              "OK": "OK",
              "Only one file is allowed.": "Un seul fichier est autorisé",
              "Open": "Ouvrir",
              "Presets": "Prérégales",
              "Reset Zoom": "Réinitialiser le Zoom",
              "Rows per page": "Lignes par page",
              "Severity": "Gravité",
              "Show/Hide Column": "Afficher/Masquer Colonnes",
              "Show Less": "Afficher moins",
              "Show More": "Afficher plus",
              "Sign In": "Connecter",
              "Sign Out": "Déconnecter",
              "Size": "Taille",
              "Subtitle": "Sous-titre",
              "Sort": "Trier",
              "TO": "À",
              "Total": "Total",
              "Type": "Type",
              "Zoom in": "Zoomer",
              "Zoom out": "Dézoomer"
            },

            // Simplified Chinese
            "zh-cn": {
              "Choose File": "选择文件",
              "Invalid file type.": "无效的文件类型。",
              "No file selected": "没有文件被选择",
              "OK": "好的",
              "Only one file is allowed.": "只有一个文件是被允许的。",
              "Open": "打开","Name": "名称",
              "Show Less": "显示更少",
              "Show More": "显示更多",
              "Size": "尺寸",
              "Type": "类型"
            }
          };
        }
      }

    }
  };
   /** @polymerBehavior */
  window.PxLocalizeBehavior = window.PxLocalizeBehavior || [Polymer.AppLocalizeBehavior, PxLocalizeBehaviorImpl];

})();
