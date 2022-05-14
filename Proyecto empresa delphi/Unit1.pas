unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, Grids, DBGrids, DB, PSQLDbTables, StdCtrls, ComCtrls, DateEdit,
  Buttons;

type
  TForm1 = class(TForm)
    BaseDatos: TPSQLDatabase;
    b_Conectar: TButton;
    b_Consultar: TButton;
    Consulta1: TPSQLQuery;
    DataSource1: TDataSource;
    DBGrid1: TDBGrid;
    b_Nuevo: TButton;
    b_Modificar: TButton;
    b_Eliminar: TButton;
    Consulta1codigousuario: TIntegerField;
    Consulta1nombre: TStringField;
    Consulta1apellido: TStringField;
    Consulta1fechanacimiento: TDateField;
    Edit1: TEdit;
    Edit2: TEdit;
    Edit3: TEdit;
    DateEdit1: TDateEdit;
    Button1: TButton;
    BitBtn1: TBitBtn;
    Button2: TButton;
    procedure b_ConectarClick(Sender: TObject);
    procedure b_ConsultarClick(Sender: TObject);
    procedure b_NuevoClick(Sender: TObject);
    procedure b_ModificarClick(Sender: TObject);
    procedure b_EliminarClick(Sender: TObject);
    procedure Edit1Change(Sender: TObject);
    procedure BitBtn1Click(Sender: TObject);
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
  private
    { Private declarations }
  public
  end;

var
  Form1: TForm1;

implementation

uses Unit2, Unit3;

{$R *.dfm}

procedure TForm1.b_ConectarClick(Sender: TObject);
begin
   //cargamos en tiempo de ejecucion las propiedades del componente de base de datos
   BaseDatos.Host :=  'localhost';
   BaseDatos.DatabaseName := 'DELPHI';
   BaseDatos.UserName := 'postgres';
   BaseDatos.UserPassword := 'admin';//poner aqui clave de usuario Postgres de su instalacion
   BaseDatos.Port := 5434;

   if BaseDatos.UserPassword  = '' then
   begin
      ShowMessage('Es necesario poner la clave antes de continuar');
      Abort; //ésta es una excepcion silenciosa
   end;
   BaseDatos.Connected := True;
   if BaseDatos.Connected then
      ShowMessage('La conexion a la base de datos se realizo con éxito')
   else
      ShowMessage('La conexion a la base de datos aun sigue sin funcionar...');
end;

procedure TForm1.b_ConsultarClick(Sender: TObject);
begin
   //En caso del componente de consulta sus propiedades ya estan cargadas en tiempo de diseño.
   //Por eso sólo queda abrir la consulta.
   Consulta1.Close; //Cierra la consulta
   Consulta1.SQL.Clear;
   Consulta1.SQL.Add('SELECT * FROM usuarios');
   Consulta1.SQL.Add('ORDER BY codigousuario ASC');
   Consulta1.Open; //Abre la consulta y muestra/refresca datos en la grilla
end;

procedure TForm1.b_NuevoClick(Sender: TObject);
begin
    Consulta1.Close;                            
    Consulta1.SQL.Clear;
    Consulta1.SQL.Add('INSERT INTO usuarios (codigousuario, nombre, apellido, fechanacimiento) VALUES (:codigousuario, :nombre, :apellido, :fechanacimiento)');
    Consulta1.ParamByName('codigousuario').value := Edit1.Text;
    Consulta1.ParamByName('nombre').value := Edit2.Text;
    Consulta1.ParamByName('apellido').value := Edit3.Text;
    Consulta1.ParamByName('fechanacimiento').value := DateEdit1.Date;
    Consulta1.ExecSQL;
    BaseDatos.StartTransaction;
    try
     BaseDatos.Commit;
     except
     BaseDatos.Rollback;
     ShowMessage('No se pudo modificar');
     raise;
    end;
    ShowMessage('Se creo el usuario Id: ' + Edit1.Text + ' nombre: '+ Edit2.Text +' apellido: '+ Edit3.Text +' fechanacimiento: '+ DateEdit1.Text);
    Consulta1.Close;



   {CONSIGNA N° 1: Crear en tiempo de ejecucion un componente de consulta e
   insertar un registro en la tabla usuarios.
   Los valores deben ser escritos en "componentes individuales" sobre el form y luego ingresar sus valores mediante SQL.
   Se recomienda uso de componente:
      TEdit -> para el codigo
      TEdit -> para el nombre y otro para el apellido
      TDateEdit -> para el ingreso de la fecha
   No olvidar incluir transaccion desde el componente de base de datos de la siguiente manera:
      BaseDatos.StartTransaction;
      Basedatos.Commit;
      BaseDatos.Rollback;
   }
   //...

end;

procedure TForm1.b_ModificarClick(Sender: TObject);
{var
   Aqui van las declaraciones de variables locales}
begin
   {CONSIGNA N° 2: Crear en tiempo de ejecucion un componente de consulta y
   modificar un registro de la tabla usuarios}
   //...
    Consulta1.Close;
    Consulta1.SQL.Clear;
    Consulta1.SQL.Add('UPDATE usuarios SET nombre = :nombre, apellido = :apellido, fechanacimiento = :fechanacimiento WHERE codigousuario = :codigousuario');
    Consulta1.ParamByName('codigousuario').value := Edit1.Text;
    Consulta1.ParamByName('nombre').value := Edit2.Text;
    Consulta1.ParamByName('apellido').value := Edit3.Text;
    Consulta1.ParamByName('fechanacimiento').value := DateEdit1.Date;
    Consulta1.ExecSQL;
    BaseDatos.StartTransaction;
    try
     BaseDatos.Commit;
     except
     BaseDatos.Rollback;
     ShowMessage('No se pudo modificar');
     raise;
    end;
    ShowMessage('Se modifico el usuario Id: ' + Edit1.Text + ' nombre: '+ Edit2.Text +' apellido: '+ Edit3.Text +' fechanacimiento: '+ DateEdit1.Text);
    Consulta1.Close;
end;

procedure TForm1.b_EliminarClick(Sender: TObject);
{var
   Aqui van las declaraciones de variables locales}
begin
   {CONSIGNA N° 3: Crear en tiempo de ejecucion un componente de consulta y
   eliminar un registro de la tabla usuarios}
   //...
   Consulta1.Close;
   Consulta1.SQL.Clear;
   Consulta1.SQL.Add('DELETE FROM usuarios WHERE codigousuario = ' + Edit1.Text);
   Consulta1.ExecSQL;
   BaseDatos.StartTransaction;
    try
     BaseDatos.Commit;
     except
     BaseDatos.Rollback;
     ShowMessage('No se pudo modificar');
     raise;
    end;
    ShowMessage('Se elimino el usuario Id: ' + Edit1.Text);
    Consulta1.Close;
end;

procedure TForm1.Edit1Change(Sender: TObject);
begin
   {consigna 4}
   Form2.Button3Click(Self);
end;

{consigna 5}

procedure TForm1.Button2Click(Sender: TObject);
begin
   Form2.Button2Click(Self);
end;
{consigna 6}
procedure TForm1.BitBtn1Click(Sender: TObject);
begin
   Form2.Button1Click(Self);
end;

{consigna 7}
procedure TForm1.Button1Click(Sender: TObject);
begin
   Form3.Show;
end;


end.
