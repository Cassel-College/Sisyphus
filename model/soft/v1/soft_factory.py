#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from model.soft.v1.soft_model import SoftModel


def create_soft(name: str, version: str) -> SoftModel:
    
    model = SoftModel(name=name, version=version)
    return model
