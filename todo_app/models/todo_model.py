# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ToDoTasks(models.Model):
    _name = 'todo.task'
    _description = 'To-Do Task'
    
    name = fields.Char('Descriptin', required = True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active', default = True)