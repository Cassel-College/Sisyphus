#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from model.soft.v1.soft_model import SoftModel


def create_soft(name: str, version: str) -> SoftModel:
    
    model = SoftModel(name=name, version=version)
    return model


def create_soft_by_dict(soft: dict) -> SoftModel:
    
    name = soft.get("name")
    version = soft.get("version")
    drive = soft.get("drive")
    shell = soft.get("shell")
    model = SoftModel(name=name,
                      version=version,
                      drive=drive,
                      shell=shell)
    return model
