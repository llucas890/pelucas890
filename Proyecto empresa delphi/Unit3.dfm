object Form3: TForm3
  Left = 325
  Top = 710
  Width = 560
  Height = 372
  Caption = 'Agregar/Modificar/Eliminar Registros por Lucas Lescano'
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'MS Sans Serif'
  Font.Style = []
  OldCreateOrder = False
  PixelsPerInch = 96
  TextHeight = 13
  object Button1: TButton
    Left = 40
    Top = 96
    Width = 89
    Height = 25
    Caption = 'Nuevo registro'
    TabOrder = 0
    OnClick = Button1Click
  end
  object Button2: TButton
    Left = 152
    Top = 96
    Width = 97
    Height = 25
    Caption = 'Modificar Registro'
    TabOrder = 1
    OnClick = Button2Click
  end
  object Button3: TButton
    Left = 272
    Top = 96
    Width = 129
    Height = 25
    Caption = 'Eliminar Registro'
    TabOrder = 2
    OnClick = Button3Click
  end
  object Edit1: TEdit
    Left = 16
    Top = 160
    Width = 121
    Height = 21
    TabOrder = 3
    Text = 'ID'
    OnChange = Edit1Change
  end
  object Edit2: TEdit
    Left = 152
    Top = 160
    Width = 121
    Height = 21
    TabOrder = 4
    Text = 'Nombre'
    OnChange = Edit2Change
  end
  object Edit3: TEdit
    Left = 288
    Top = 160
    Width = 121
    Height = 21
    TabOrder = 5
    Text = 'Apellido'
    OnChange = Edit3Change
  end
  object DateEdit1: TDateEdit
    Left = 432
    Top = 160
    Width = 68
    Height = 21
    ColorTextErr = clRed
    ColorTextOK = clBlack
    DateFormat = 'dd/mm/yyyy'
    TabOrder = 6
    UseOSDateFormat = False
    ZeroDateIsValid = True
    OnChange = DateEdit1Change
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
      'Host=localhost'
      'UID=postgres'
      'PWD=admin')
    Port = 5434
    UserName = 'postgres'
    UserPassword = 'admin'
    Left = 8
    Top = 8
  end
  object PSQLQuery1: TPSQLQuery
    Database = PSQLDatabase1
    Options = [dsoUseGUIDField]
    Left = 40
    Top = 8
  end
end
