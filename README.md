[![Build](https://github.com/fga-eps-mds/2021.2-SysArq-Profile/workflows/Compilação/badge.svg)](https://github.com/fga-eps-mds/2021.2-SysArq-Profile/actions/workflows/build.yml)
[![Style](https://github.com/fga-eps-mds/2021.2-SysArq-Profile/workflows/Estilo/badge.svg)](https://github.com/fga-eps-mds/2021.2-SysArq-Profile/actions/workflows/style.yml)
[![Tests](https://github.com/fga-eps-mds/2021.2-SysArq-Profile/workflows/Testes/badge.svg)](https://github.com/fga-eps-mds/2021.2-SysArq-Profile/actions/workflows/test.yml)

# API de Gerenciamento de Usuários do SysArq

[![codecov](https://codecov.io/gh/fga-eps-mds/2021.2-SysArq-Profile/branch/main/graph/badge.svg?token=CVD5NRJMN5)](https://codecov.io/gh/fga-eps-mds/2021.2-SysArq-Profile)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=fga-eps-mds_2021.2-SysArq-Profile&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=fga-eps-mds_2021.2-SysArq-Profile)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=fga-eps-mds_2021.2-SysArq-Profile&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=fga-eps-mds_2021.2-SysArq-Profile)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=fga-eps-mds_2021.2-SysArq-Profile&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=fga-eps-mds_2021.2-SysArq-Profile)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=fga-eps-mds_2021.2-SysArq-Profile&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=fga-eps-mds_2021.2-SysArq-Profile)

[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=fga-eps-mds_2021.2-SysArq-Profile&metric=bugs)](https://sonarcloud.io/summary/new_code?id=fga-eps-mds_2021.2-SysArq-Profile)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=fga-eps-mds_2021.2-SysArq-Profile&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=fga-eps-mds_2021.2-SysArq-Profile)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=fga-eps-mds_2021.2-SysArq-Profile&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=fga-eps-mds_2021.2-SysArq-Profile)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=fga-eps-mds_2021.2-SysArq-Profile&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=fga-eps-mds_2021.2-SysArq-Profile)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=fga-eps-mds_2021.2-SysArq-Profile&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=fga-eps-mds_2021.2-SysArq-Profile)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=fga-eps-mds_2021.2-SysArq-Profile&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=fga-eps-mds_2021.2-SysArq-Profile)

A API de Gerenciamento de Arquivos do *SysArq* compõe a arquitetura de microsserviços do sistema *[SysArq](https://fga-eps-mds.github.io/2021-2-SysArq-Doc/)*.

Esse microsserviço é responsável pelo *CRUD* ([veja a definição](https://developer.mozilla.org/pt-BR/docs/Glossary/CRUD)), autenticação e gerenciamento de permissões de usuário da aplicação. **[Saiba mais](https://fga-eps-mds.github.io/2021-2-SysArq-Doc/documentation/)**

## Execução

### Requisitos
 - ***`Docker`*** - [veja como instalar](https://docs.docker.com/engine/install/);
 - ***`docker-compose`***, no mínimo a versão *`1.29.0`* - [veja como instalar](https://docs.docker.com/compose/install/).

### Executar

1. Clone esse repositório - [veja como clonar um repositório](https://docs.github.com/pt/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository);

2. Crie, utilizando o arquivo ***env-reference***, o *`.env`* dentro da **pasta do repositório**;

3. Execute, dentro da **pasta do repositório**, o comando:
   ```
    sudo docker-compose up
   ```

4. Acesse [http://0.0.0.0:8001/](http://0.0.0.0:8001) no navegador. 

### Testes e Verificação de Estilo

-  Para **testar** a aplicação, utilize o ***pytest***. Por exemplo:
   ```
      sudo docker-compose run web pytest --cov
   ```
   **Observação**: Só serão aceitas contribuições com 90% de cobertura de código.

- Para **verificar o estilo de código** da aplicação, utilize o ***flake8***. Por exemplo:
   ```
      sudo docker-compose run web flake8
   ```
   **Observação**: Só serão aceitas contribuições com o estilo correto.

**ATENÇÃO**: Execute os comandos dentro da **`pasta`** do repositório.

## Documentação

### Como contribuir
- Leia o [guia de contribuição](CONTRIBUTING.md).
