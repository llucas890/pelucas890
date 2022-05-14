object Form2: TForm2
  Left = 1154
  Top = 211
  Width = 668
  Height = 387
  Caption = 'Form2'
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'MS Sans Serif'
  Font.Style = []
  OldCreateOrder = False
  PixelsPerInch = 96
  TextHeight = 13
  object DBGrid1: TDBGrid
    Left = 160
    Top = 80
    Width = 49
    Height = 33
    Options = [dgEditing, dgAlwaysShowEditor, dgTitles, dgIndicator, dgColumnResize, dgColLines, dgRowLines, dgTabs, dgConfirmDelete]
    TabOrder = 0
    TitleFont.Charset = DEFAULT_CHARSET
    TitleFont.Color = clWindowText
    TitleFont.Height = -11
    TitleFont.Name = 'MS Sans Serif'
    TitleFont.Style = []
    Columns = <
      item
        Expanded = False
        FieldName = 'codigousuario'
        Visible = True
      end>
  end
  object Button1: TButton
    Left = 96
    Top = 48
    Width = 225
    Height = 177
    Caption = 'Cantidad de Registros'
    TabOrder = 1
    OnClick = Button1Click
  end
  object Button2: TButton
    Left = 344
    Top = 48
    Width = 193
    Height = 177
    Caption = 'Ver id recomendado'
    TabOrder = 2
    OnClick = Button2Click
  end
  object Button3: TButton
    Left = 336
    Top = 240
    Width = 209
    Height = 105
    Caption = 'Button3'
    TabOrder = 3
    OnClick = Button3Click
  end
  object PSQLDatabase1: TPSQLDatabase
    CharSet = 'LATIN1'
    DatabaseName = 'DELPHI'
    Host = 'localhost'
    Params.Strings = (
      'ConnectionTimeout=15'
      'Port=5434'
      'SSLMode=prefer'
      'DatabaseName=DELPHI'
      'UID=postgres'
      'PWD=admin'
      'Host=localhost')
    Port = 5434
    UserName = 'postgres'
    UserPassword = 'admin'
    Left = 136
    Top = 272
  end
  object Consulta2: TPSQLQuery
    Database = PSQLDatabase1
    Options = [dsoUseGUIDField]
    Left = 192
    Top = 272
  end
end
