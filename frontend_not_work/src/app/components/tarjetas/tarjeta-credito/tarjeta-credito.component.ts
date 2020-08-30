import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-tarjeta-credito',
  templateUrl: './tarjeta-credito.component.html',
  styleUrls: ['./tarjeta-credito.component.css']
})
export class TarjetaCreditoComponent implements OnInit {
  form: FormGroup;

  constructor(private formBuilder: FormBuilder) {
    this.form = this.formBuilder.group(
      {
        id: 0,
        titular: ['', [Validators.required]],
        numeroTarjeta: ['', [Validators.required, Validators.maxLength(16), Validators.minLength(16)]],
        fechaExpiracion: ['', [Validators.required, Validators.maxLength(8), Validators.minLength(8)]],
        cvv: ['', [Validators.required, Validators.maxLength(3), Validators.minLength(3)]],
      }
    )
  }

  ngOnInit(): void {
  }

  guardarEvento() {
    console.log(this.form);
  }

}