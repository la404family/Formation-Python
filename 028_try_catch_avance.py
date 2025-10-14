#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================
TRY/CATCH AVANCÉ EN PYTHON - GUIDE COMPLET
======================================================================

🎯 Ce fichier couvre les techniques avancées de gestion d'erreurs :
   • Patterns de gestion d'exceptions sophistiqués
   • Exception chaining et context
   • Custom exception hierarchies
   • Error handling strategies
   • Monitoring et logging d'erreurs
   • Recovery patterns et resilience

📚 Concepts abordés :
   • Exception groups et handling avancé
   • Decorators pour error handling
   • Circuit breakers et retry patterns
   • Error aggregation et reporting
   • Graceful degradation
   • Fault tolerance architectures

💡 Objectif : Maîtriser la gestion robuste des erreurs
"""

from contextlib import suppress
import os
import logging
import time
import traceback
from functools import wraps
from typing import List, Dict, Any, Optional, Callable
from dataclasses import dataclass
from datetime import datetime, timedelta
import json

print("=" * 70)
print("TRY/CATCH AVANCÉ EN PYTHON - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. EXCEPTION CHAINING AVANCÉ")
print("=" * 50)

print("\n🔗 CHAÎNAGE D'EXCEPTIONS")
print("-" * 24)


class BusinessError(Exception):
    """Exception métier de base"""

    def __init__(self, message: str, error_code: str = None, context: Dict = None):
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.context = context or {}
        self.timestamp = datetime.now()


class ValidationError(BusinessError):
    """Erreur de validation"""
    pass


class DataProcessingError(BusinessError):
    """Erreur de traitement de données"""
    pass


class ExternalServiceError(BusinessError):
    """Erreur de service externe"""
    pass


def demo_exception_chaining():
    """Démonstration du chaînage d'exceptions avancé"""

    print("🔗 Chaînage d'exceptions avancé :")

    def valider_donnees(donnees):
        """Validation avec exceptions chaînées"""
        try:
            if not isinstance(donnees, dict):
                raise TypeError(f"Dictionnaire attendu, reçu {type(donnees)}")

            if "email" not in donnees:
                raise KeyError("Champ 'email' manquant")

            email = donnees["email"]
            if "@" not in email:
                raise ValueError(f"Format email invalide : {email}")

        except (TypeError, KeyError, ValueError) as e:
            # Chaîner avec une exception métier
            raise ValidationError(
                f"Validation échouée pour les données utilisateur",
                error_code="VALIDATION_FAILED",
                context={"donnees": str(donnees)[:100]}
            ) from e

    def traiter_utilisateur(donnees):
        """Traitement avec chaînage à plusieurs niveaux"""
        try:
            valider_donnees(donnees)

            # Simulation d'une erreur de traitement
            if donnees.get("nom") == "ERROR":
                raise RuntimeError("Erreur simulée de traitement")

            return {"status": "success", "user_id": 12345}

        except ValidationError:
            raise  # Re-propager sans modifier
        except Exception as e:
            # Chaîner avec une nouvelle exception métier
            raise DataProcessingError(
                "Erreur lors du traitement utilisateur",
                error_code="PROCESSING_FAILED",
                context={"donnees": donnees}
            ) from e

    # Tests avec différents types d'erreurs
    test_cases = [
        ({"email": "test@example.com", "nom": "Alice"}, "Cas valide"),
        ({"nom": "Bob"}, "Email manquant"),
        ({"email": "invalid-email", "nom": "Charlie"}, "Email invalide"),
        ("not-a-dict", "Type incorrect"),
        ({"email": "test@example.com", "nom": "ERROR"}, "Erreur de traitement"),
    ]

    for donnees, description in test_cases:
        print(f"\n   Test : {description}")
        try:
            resultat = traiter_utilisateur(donnees)
            print(f"   ✅ Succès : {resultat}")
        except BusinessError as e:
            print(f"   ❌ {type(e).__name__} : {e.message}")
            print(f"      Code : {e.error_code}")
            print(f"      Contexte : {e.context}")

            # Afficher la chaîne d'exceptions
            current = e
            level = 0
            while current:
                print(
                    f"      {'  ' * level}↳ {type(current).__name__}: {current}")
                current = current.__cause__
                level += 1


demo_exception_chaining()

print("\n🎯 EXCEPTION CONTEXT ET SUPPRESS")
print("-" * 33)


def demo_exception_context():
    """Démonstration du contexte d'exception et suppress"""

    print("🎯 Exception context et suppress :")

    # Utilisation de suppress pour ignorer des exceptions spécifiques
    print("\n   1️⃣ Suppression d'exceptions avec contextlib.suppress :")

    def operations_avec_suppress():
        """Opérations avec suppression sélective d'erreurs"""
        resultats = []

        # Tentatives d'opérations qui peuvent échouer
        operations = [
            lambda: int("123"),      # Succès
            lambda: int("invalid"),  # ValueError
            lambda: 10 / 2,          # Succès
            lambda: 10 / 0,          # ZeroDivisionError
            lambda: [1, 2, 3][1],      # Succès
            lambda: [1, 2, 3][10],     # IndexError
        ]

        for i, operation in enumerate(operations):
            print(f"      Opération {i+1} :", end=" ")

            # Supprimer certaines erreurs attendues
            with suppress(ValueError, ZeroDivisionError, IndexError):
                result = operation()
                resultats.append(result)
                print(f"✅ Résultat: {result}")
                continue

            # Si on arrive ici, l'opération a été supprimée
            print("❌ Erreur supprimée")
            resultats.append(None)

        return resultats

    resultats = operations_avec_suppress()
    print(f"      Résultats finaux : {resultats}")

    # Comparison avec gestion manuelle
    print("\n   2️⃣ Comparaison avec gestion manuelle :")

    def operations_manuelles():
        """Même chose avec gestion manuelle"""
        resultats = []

        operations = [
            lambda: int("123"),
            lambda: int("invalid"),
            lambda: 10 / 2,
            lambda: 10 / 0,
        ]

        for i, operation in enumerate(operations):
            try:
                result = operation()
                resultats.append(result)
                print(f"      Opération {i+1} : ✅ {result}")
            except (ValueError, ZeroDivisionError) as e:
                resultats.append(None)
                print(f"      Opération {i+1} : ❌ {type(e).__name__}")

        return resultats

    resultats_manuels = operations_manuelles()
    print(f"      Résultats manuels : {resultats_manuels}")


demo_exception_context()

print("\n" + "=" * 50)
print("2. DECORATORS POUR ERROR HANDLING")
print("=" * 50)

print("\n🎨 DÉCORATEURS DE GESTION D'ERREURS")
print("-" * 35)


def retry(max_attempts: int = 3, delay: float = 1.0, backoff: float = 2.0,
          exceptions: tuple = (Exception,)):
    """Décorateur de retry avec backoff exponentiel"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay

            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_attempts - 1:
                        print(
                            f"   💥 Échec définitif après {max_attempts} tentatives")
                        raise

                    print(f"   ❌ Tentative {attempt + 1} échouée : {e}")
                    print(f"   ⏳ Attente de {current_delay:.1f}s avant retry")

                    time.sleep(current_delay)
                    current_delay *= backoff

            return None  # Ne devrait jamais arriver

        return wrapper
    return decorator


def handle_exceptions(*exception_types, default_return=None, log_errors=True):
    """Décorateur pour gestion automatique d'exceptions"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception_types as e:
                if log_errors:
                    print(
                        f"   🚨 Exception gérée dans {func.__name__}: {type(e).__name__}: {e}")
                return default_return
            except Exception as e:
                if log_errors:
                    print(
                        f"   💥 Exception non gérée dans {func.__name__}: {type(e).__name__}: {e}")
                raise

        return wrapper
    return decorator


def measure_performance(include_errors=True):
    """Décorateur pour mesurer les performances avec gestion d'erreurs"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            success = True
            error_info = None

            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                success = False
                error_info = {"type": type(e).__name__, "message": str(e)}
                if include_errors:
                    raise
                return None
            finally:
                end_time = time.time()
                duration = end_time - start_time

                status = "✅ SUCCESS" if success else "❌ ERROR"
                print(f"   📊 {func.__name__} : {status} en {duration:.3f}s")

                if error_info:
                    print(
                        f"      Erreur : {error_info['type']}: {error_info['message']}")

        return wrapper
    return decorator


def demo_decorators_error_handling():
    """Démonstration des décorateurs de gestion d'erreurs"""

    print("🎨 Décorateurs de gestion d'erreurs :")

    # Fonction instable pour les tests
    call_count = 0

    @retry(max_attempts=3, delay=0.1, exceptions=(RuntimeError, ValueError))
    @measure_performance()
    def operation_instable(taux_succes=0.3):
        """Opération qui échoue souvent"""
        nonlocal call_count
        call_count += 1

        import random
        if random.random() < taux_succes:
            return f"Succès à l'appel {call_count}"
        else:
            raise RuntimeError(f"Échec simulé à l'appel {call_count}")

    print("\n   1️⃣ Test du décorateur retry :")
    call_count = 0
    try:
        # Très faible chance de succès
        resultat = operation_instable(taux_succes=0.1)
        print(f"   🎉 Résultat : {resultat}")
    except Exception as e:
        print(f"   💀 Échec final : {e}")

    # Fonction avec gestion automatique d'erreurs
    @handle_exceptions(ValueError, TypeError, default_return="Erreur gérée")
    @measure_performance(include_errors=False)
    def operation_avec_gestion(valeur):
        """Opération avec gestion automatique d'erreurs"""
        if valeur == "error":
            raise ValueError("Erreur de valeur simulée")
        elif valeur == "type_error":
            raise TypeError("Erreur de type simulée")
        elif valeur == "runtime_error":
            raise RuntimeError("Cette erreur ne sera pas gérée")
        else:
            return f"Traitement réussi : {valeur.upper()}"

    print("\n   2️⃣ Test du décorateur handle_exceptions :")
    test_values = ["hello", "error", "type_error", "runtime_error"]

    for valeur in test_values:
        print(f"      Test avec '{valeur}' :", end=" ")
        try:
            resultat = operation_avec_gestion(valeur)
            print(f"Résultat: {resultat}")
        except Exception as e:
            print(f"Exception non gérée: {type(e).__name__}")


demo_decorators_error_handling()

print("\n🔧 DÉCORATEUR DE VALIDATION")
print("-" * 26)


def validate_args(**validators):
    """Décorateur de validation d'arguments"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Récupérer les noms des paramètres
            import inspect
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()

            # Valider chaque argument
            for param_name, validator in validators.items():
                if param_name in bound_args.arguments:
                    value = bound_args.arguments[param_name]

                    try:
                        if callable(validator):
                            if not validator(value):
                                raise ValidationError(
                                    f"Validation échouée pour {param_name}: {value}",
                                    error_code="VALIDATION_FAILED"
                                )
                        elif isinstance(validator, type):
                            if not isinstance(value, validator):
                                raise ValidationError(
                                    f"Type incorrect pour {param_name}: attendu {validator.__name__}, reçu {type(value).__name__}",
                                    error_code="TYPE_MISMATCH"
                                )
                    except ValidationError:
                        raise
                    except Exception as e:
                        raise ValidationError(
                            f"Erreur de validation pour {param_name}: {e}",
                            error_code="VALIDATION_ERROR"
                        ) from e

            return func(*args, **kwargs)

        return wrapper
    return decorator


def demo_validation_decorator():
    """Test du décorateur de validation"""

    print("🔧 Décorateur de validation :")

    @validate_args(
        nom=str,
        age=lambda x: isinstance(x, int) and 0 <= x <= 150,
        email=lambda x: isinstance(x, str) and "@" in x,
        actif=bool
    )
    def creer_utilisateur(nom: str, age: int, email: str, actif: bool = True):
        """Créer un utilisateur avec validation automatique"""
        return {
            "nom": nom,
            "age": age,
            "email": email,
            "actif": actif,
            "id": hash(f"{nom}{email}") % 10000
        }

    # Tests de validation
    test_cases = [
        (("Alice", 25, "alice@test.com"), {}, "Cas valide"),
        (("Bob",), {"age": 30, "email": "bob@test.com"}, "Avec kwargs"),
        (("Charlie", -5, "charlie@test.com"), {}, "Âge négatif"),
        (("Diane", 30, "invalid-email"), {}, "Email invalide"),
        ((123, 25, "test@test.com"), {}, "Nom non-string"),
        (("Eve", "trente", "eve@test.com"), {}, "Âge non-int"),
    ]

    for args, kwargs, description in test_cases:
        print(f"\n   Test : {description}")
        try:
            utilisateur = creer_utilisateur(*args, **kwargs)
            print(f"   ✅ Utilisateur créé : {utilisateur}")
        except ValidationError as e:
            print(f"   ❌ Validation échouée : {e.message}")
            print(f"      Code : {e.error_code}")


demo_validation_decorator()

print("\n" + "=" * 50)
print("3. CIRCUIT BREAKER PATTERN")
print("=" * 50)

print("\n⚡ CIRCUIT BREAKER AVANCÉ")
print("-" * 26)


@dataclass
class CircuitBreakerStats:
    """Statistiques du circuit breaker"""
    total_calls: int = 0
    successful_calls: int = 0
    failed_calls: int = 0
    timeouts: int = 0
    last_failure_time: Optional[datetime] = None
    consecutive_failures: int = 0


class CircuitBreakerState:
    """États du circuit breaker"""
    CLOSED = "CLOSED"      # Normal, laisse passer les appels
    OPEN = "OPEN"          # Bloque les appels après trop d'échecs
    HALF_OPEN = "HALF_OPEN"  # Test de récupération


class AdvancedCircuitBreaker:
    """Circuit breaker avancé avec métriques et stratégies"""

    def __init__(self,
                 failure_threshold: int = 5,
                 timeout_seconds: float = 60.0,
                 expected_exceptions: tuple = (Exception,),
                 success_threshold: int = 3):
        self.failure_threshold = failure_threshold
        self.timeout_seconds = timeout_seconds
        self.expected_exceptions = expected_exceptions
        self.success_threshold = success_threshold

        self.state = CircuitBreakerState.CLOSED
        self.stats = CircuitBreakerStats()
        self.half_open_successes = 0

    def _should_attempt_reset(self) -> bool:
        """Vérifier si on doit tenter de fermer le circuit"""
        if self.stats.last_failure_time is None:
            return False

        time_since_failure = datetime.now() - self.stats.last_failure_time
        return time_since_failure.total_seconds() >= self.timeout_seconds

    def _record_success(self):
        """Enregistrer un succès"""
        self.stats.total_calls += 1
        self.stats.successful_calls += 1
        self.stats.consecutive_failures = 0

        if self.state == CircuitBreakerState.HALF_OPEN:
            self.half_open_successes += 1
            if self.half_open_successes >= self.success_threshold:
                self.state = CircuitBreakerState.CLOSED
                self.half_open_successes = 0
                print(f"   🔄 Circuit fermé : service rétabli")

    def _record_failure(self, exception):
        """Enregistrer un échec"""
        self.stats.total_calls += 1
        self.stats.failed_calls += 1
        self.stats.consecutive_failures += 1
        self.stats.last_failure_time = datetime.now()

        if isinstance(exception, TimeoutError):
            self.stats.timeouts += 1

        if self.state == CircuitBreakerState.HALF_OPEN:
            self.state = CircuitBreakerState.OPEN
            self.half_open_successes = 0
            print(f"   🚨 Circuit rouvert : nouvelle panne détectée")
        elif (self.state == CircuitBreakerState.CLOSED and
              self.stats.consecutive_failures >= self.failure_threshold):
            self.state = CircuitBreakerState.OPEN
            print(
                f"   🚨 Circuit ouvert : {self.stats.consecutive_failures} échecs consécutifs")

    def get_stats(self) -> Dict[str, Any]:
        """Obtenir les statistiques"""
        success_rate = 0
        if self.stats.total_calls > 0:
            success_rate = (self.stats.successful_calls /
                            self.stats.total_calls) * 100

        return {
            "state": self.state,
            "total_calls": self.stats.total_calls,
            "success_rate": f"{success_rate:.1f}%",
            "consecutive_failures": self.stats.consecutive_failures,
            "last_failure": self.stats.last_failure_time.isoformat() if self.stats.last_failure_time else None
        }

    def call(self, func, *args, **kwargs):
        """Appeler une fonction avec protection circuit breaker"""

        # Vérifier l'état du circuit
        if self.state == CircuitBreakerState.OPEN:
            if self._should_attempt_reset():
                self.state = CircuitBreakerState.HALF_OPEN
                print(f"   🔄 Circuit semi-ouvert : test de récupération")
            else:
                raise RuntimeError(
                    f"Circuit breaker ouvert. "
                    f"Prochain test dans {self.timeout_seconds - (datetime.now() - self.stats.last_failure_time).total_seconds():.1f}s"
                )

        # Tenter l'appel
        try:
            result = func(*args, **kwargs)
            self._record_success()
            return result

        except self.expected_exceptions as e:
            self._record_failure(e)
            raise

    def __call__(self, func):
        """Utiliser comme décorateur"""
        @wraps(func)
        def wrapper(*args, **kwargs):
            return self.call(func, *args, **kwargs)
        return wrapper


def demo_circuit_breaker():
    """Démonstration du circuit breaker avancé"""

    print("⚡ Circuit breaker avancé :")

    # Créer un circuit breaker
    cb = AdvancedCircuitBreaker(
        failure_threshold=3,
        timeout_seconds=2.0,
        success_threshold=2
    )

    # Service instable pour les tests
    call_counter = 0

    def service_instable(taux_echec=0.7):
        """Service qui échoue selon un taux donné"""
        nonlocal call_counter
        call_counter += 1

        import random
        if random.random() < taux_echec:
            raise RuntimeError(f"Service indisponible (appel {call_counter})")

        return f"Service OK (appel {call_counter})"

    # Test avec taux d'échec élevé
    print(f"\n   1️⃣ Test avec taux d'échec élevé (70%) :")

    for i in range(10):
        try:
            result = cb.call(service_instable, taux_echec=0.7)
            print(f"   ✅ Appel {i+1} : {result}")
        except Exception as e:
            print(f"   ❌ Appel {i+1} : {type(e).__name__}: {e}")

        # Afficher les stats périodiquement
        if (i+1) % 3 == 0:
            stats = cb.get_stats()
            print(f"      📊 Stats : {stats}")

        time.sleep(0.1)

    # Attendre la récupération
    print(f"\n   2️⃣ Attente de récupération...")
    time.sleep(2.1)

    # Test avec taux d'échec plus faible
    print(f"   3️⃣ Test avec service amélioré (20% échec) :")

    for i in range(5):
        try:
            result = cb.call(service_instable, taux_echec=0.2)
            print(f"   ✅ Appel récupération {i+1} : {result}")
        except Exception as e:
            print(f"   ❌ Appel récupération {i+1} : {type(e).__name__}: {e}")

        time.sleep(0.1)

    # Stats finales
    stats_finales = cb.get_stats()
    print(f"\n   📊 Statistiques finales : {stats_finales}")


demo_circuit_breaker()

print("\n" + "=" * 50)
print("4. ERROR AGGREGATION ET REPORTING")
print("=" * 50)

print("\n📊 COLLECTE ET AGRÉGATION D'ERREURS")
print("-" * 35)


class ErrorCollector:
    """Collecteur d'erreurs avec agrégation et reporting"""

    def __init__(self):
        self.errors: List[Dict[str, Any]] = []
        self.error_counts: Dict[str, int] = {}
        self.start_time = datetime.now()

    def record_error(self,
                     exception: Exception,
                     context: Dict[str, Any] = None,
                     severity: str = "ERROR"):
        """Enregistrer une erreur"""

        error_info = {
            "timestamp": datetime.now().isoformat(),
            "type": type(exception).__name__,
            "message": str(exception),
            "severity": severity,
            "context": context or {},
            "traceback": traceback.format_exc() if hasattr(exception, '__traceback__') else None
        }

        self.errors.append(error_info)

        # Comptage par type
        error_type = type(exception).__name__
        self.error_counts[error_type] = self.error_counts.get(
            error_type, 0) + 1

    def get_error_summary(self) -> Dict[str, Any]:
        """Obtenir un résumé des erreurs"""
        total_errors = len(self.errors)
        uptime = (datetime.now() - self.start_time).total_seconds()

        # Top 5 des erreurs les plus fréquentes
        sorted_errors = sorted(self.error_counts.items(),
                               key=lambda x: x[1], reverse=True)
        top_errors = sorted_errors[:5]

        # Erreurs par niveau de sévérité
        severity_counts = {}
        for error in self.errors:
            severity = error["severity"]
            severity_counts[severity] = severity_counts.get(severity, 0) + 1

        # Erreurs récentes (dernière heure)
        one_hour_ago = datetime.now() - timedelta(hours=1)
        recent_errors = [
            error for error in self.errors
            if datetime.fromisoformat(error["timestamp"]) > one_hour_ago
        ]

        return {
            "total_errors": total_errors,
            "uptime_seconds": uptime,
            "errors_per_hour": len(recent_errors),
            "top_error_types": top_errors,
            "severity_breakdown": severity_counts,
            "recent_errors_count": len(recent_errors)
        }

    def get_detailed_report(self) -> str:
        """Générer un rapport détaillé"""
        summary = self.get_error_summary()

        report = [
            "=" * 50,
            "RAPPORT D'ERREURS DÉTAILLÉ",
            "=" * 50,
            f"Période : {self.start_time.strftime('%Y-%m-%d %H:%M:%S')} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"Durée : {summary['uptime_seconds']:.1f} secondes",
            f"Total erreurs : {summary['total_errors']}",
            f"Erreurs par heure : {summary['errors_per_hour']}",
            "",
            "TOP ERREURS :",
        ]

        for error_type, count in summary["top_error_types"]:
            percentage = (count / summary["total_errors"]) * 100
            report.append(f"  • {error_type}: {count} ({percentage:.1f}%)")

        report.extend([
            "",
            "RÉPARTITION PAR SÉVÉRITÉ :",
        ])

        for severity, count in summary["severity_breakdown"].items():
            report.append(f"  • {severity}: {count}")

        if summary["recent_errors_count"] > 0:
            report.extend([
                "",
                "ERREURS RÉCENTES (dernière heure) :",
            ])

            one_hour_ago = datetime.now() - timedelta(hours=1)
            recent_errors = [
                error for error in self.errors[-10:]  # 10 dernières
                if datetime.fromisoformat(error["timestamp"]) > one_hour_ago
            ]

            for error in recent_errors:
                timestamp = error["timestamp"].split(
                    ".")[0]  # Sans microsecondes
                report.append(
                    f"  • [{timestamp}] {error['type']}: {error['message']}")

        return "\n".join(report)


class ErrorHandler:
    """Gestionnaire d'erreurs avec collecte automatique"""

    def __init__(self):
        self.collector = ErrorCollector()

    def handle_error(self, exception: Exception, context: Dict[str, Any] = None,
                     severity: str = "ERROR", re_raise: bool = True):
        """Gérer une erreur avec collecte automatique"""

        self.collector.record_error(exception, context, severity)

        # Log l'erreur
        print(f"   🚨 [{severity}] {type(exception).__name__}: {exception}")
        if context:
            print(f"      Context: {context}")

        if re_raise:
            raise exception

    def safe_execute(self, func, *args, **kwargs):
        """Exécuter une fonction avec gestion d'erreurs automatique"""
        try:
            return func(*args, **kwargs)
        except Exception as e:
            context = {
                "function": func.__name__,
                "args": str(args)[:100],
                "kwargs": str(kwargs)[:100]
            }
            self.handle_error(e, context, re_raise=False)
            return None

    def get_summary(self):
        """Obtenir le résumé des erreurs"""
        return self.collector.get_error_summary()

    def get_report(self):
        """Obtenir le rapport détaillé"""
        return self.collector.get_detailed_report()


def demo_error_aggregation():
    """Démonstration de l'agrégation d'erreurs"""

    print("📊 Collecte et agrégation d'erreurs :")

    error_handler = ErrorHandler()

    # Simuler différents types d'erreurs
    def fonction_qui_echoue(error_type):
        """Fonction qui génère différents types d'erreurs"""
        if error_type == "value":
            raise ValueError("Valeur incorrecte")
        elif error_type == "type":
            raise TypeError("Type incorrect")
        elif error_type == "runtime":
            raise RuntimeError("Erreur d'exécution")
        elif error_type == "custom":
            raise BusinessError("Erreur métier", error_code="BIZ_001")
        else:
            return f"Succès pour {error_type}"

    # Générer plusieurs erreurs
    print("\n   1️⃣ Génération d'erreurs multiples :")

    test_scenarios = [
        ("value", {"user_id": 123, "action": "validation"}),
        ("success", {"user_id": 456, "action": "normal"}),
        ("type", {"user_id": 789, "action": "conversion"}),
        ("value", {"user_id": 101, "action": "validation"}),  # Répétition
        ("runtime", {"user_id": 102, "action": "processing"}),
        ("custom", {"user_id": 103, "action": "business_logic"}),
        ("type", {"user_id": 104, "action": "conversion"}),  # Répétition
    ]

    for error_type, context in test_scenarios:
        result = error_handler.safe_execute(fonction_qui_echoue, error_type)
        if result:
            print(f"   ✅ {error_type}: {result}")

    # Afficher le résumé
    print("\n   2️⃣ Résumé des erreurs :")
    summary = error_handler.get_summary()
    for key, value in summary.items():
        print(f"      {key}: {value}")

    # Rapport détaillé
    print("\n   3️⃣ Rapport détaillé :")
    report = error_handler.get_report()
    print(report)


demo_error_aggregation()

print("\n" + "=" * 50)
print("5. GRACEFUL DEGRADATION")
print("=" * 50)

print("\n🛡️ STRATÉGIES DE DÉGRADATION GRACIEUSE")
print("-" * 39)


class ServiceLevel:
    """Niveaux de service pour dégradation gracieuse"""
    FULL = "FULL"           # Service complet
    DEGRADED = "DEGRADED"   # Service dégradé
    LIMITED = "LIMITED"     # Service limité
    OFFLINE = "OFFLINE"     # Service hors ligne


class GracefulService:
    """Service avec dégradation gracieuse"""

    def __init__(self, name: str):
        self.name = name
        self.level = ServiceLevel.FULL
        self.error_count = 0
        self.error_threshold = 3
        self.degradation_timeout = 5.0
        self.last_error_time = None
        self.fallback_data = {}

    def _update_service_level(self):
        """Mettre à jour le niveau de service basé sur les erreurs"""
        if self.error_count == 0:
            self.level = ServiceLevel.FULL
        elif self.error_count < self.error_threshold:
            self.level = ServiceLevel.DEGRADED
        elif self.error_count < self.error_threshold * 2:
            self.level = ServiceLevel.LIMITED
        else:
            self.level = ServiceLevel.OFFLINE

    def _should_recover(self) -> bool:
        """Vérifier si le service peut tenter de récupérer"""
        if self.last_error_time is None:
            return True

        time_since_error = time.time() - self.last_error_time
        return time_since_error > self.degradation_timeout

    def _record_error(self):
        """Enregistrer une erreur"""
        self.error_count += 1
        self.last_error_time = time.time()
        self._update_service_level()
        print(
            f"   ⚠️ Service {self.name} dégradé : niveau {self.level} ({self.error_count} erreurs)")

    def _record_success(self):
        """Enregistrer un succès"""
        if self.error_count > 0:
            self.error_count = max(0, self.error_count - 1)
            old_level = self.level
            self._update_service_level()
            if old_level != self.level:
                print(
                    f"   ✅ Service {self.name} amélioré : niveau {self.level}")

    def call_with_fallback(self, primary_func, fallback_func=None, *args, **kwargs):
        """Appeler une fonction avec fallback selon le niveau de service"""

        # Tentative de récupération
        if self.level != ServiceLevel.FULL and self._should_recover():
            print(f"   🔄 Tentative de récupération pour {self.name}")

        # Selon le niveau de service
        if self.level == ServiceLevel.OFFLINE:
            print(
                f"   💀 Service {self.name} hors ligne - utilisation du cache")
            return self.fallback_data.get("last_result", "Service indisponible")

        try:
            # Appel principal avec adaptations selon le niveau
            if self.level == ServiceLevel.LIMITED:
                # Mode limité : timeout réduit, fonctionnalités de base seulement
                print(f"   ⚡ Service {self.name} en mode limité")
                kwargs.setdefault('timeout', 1.0)
            elif self.level == ServiceLevel.DEGRADED:
                # Mode dégradé : moins de fonctionnalités
                print(f"   ⚠️ Service {self.name} en mode dégradé")
                kwargs.setdefault('timeout', 2.0)

            result = primary_func(*args, **kwargs)
            self._record_success()

            # Sauvegarder pour le cache
            self.fallback_data["last_result"] = result

            return result

        except Exception as e:
            print(f"   ❌ Erreur dans {self.name}: {e}")
            self._record_error()

            # Utiliser le fallback si disponible
            if fallback_func:
                try:
                    print(f"   🔄 Utilisation du fallback pour {self.name}")
                    fallback_result = fallback_func(*args, **kwargs)
                    return fallback_result
                except Exception as fallback_error:
                    print(f"   💥 Fallback échoué: {fallback_error}")

            # Dernier recours : données en cache
            if "last_result" in self.fallback_data:
                print(f"   💾 Utilisation des données en cache")
                return self.fallback_data["last_result"]

            # Si tout échoue
            if self.level == ServiceLevel.LIMITED:
                return "Service temporairement indisponible"
            else:
                raise


def demo_graceful_degradation():
    """Démonstration de la dégradation gracieuse"""

    print("🛡️ Dégradation gracieuse de services :")

    # Service de géolocalisation
    geo_service = GracefulService("Géolocalisation")

    def get_location_full(user_id, timeout=5.0):
        """Service de géolocalisation complet"""
        import random

        # Simuler des pannes aléatoirement
        if random.random() < 0.4:  # 40% de chance d'échec
            raise RuntimeError("Service de géolocalisation indisponible")

        # Simuler timeout
        if timeout < 2.0:
            raise TimeoutError("Timeout du service de géolocalisation")

        return {
            "user_id": user_id,
            "latitude": 48.8566 + random.uniform(-0.1, 0.1),
            "longitude": 2.3522 + random.uniform(-0.1, 0.1),
            "accuracy": "high",
            "timestamp": datetime.now().isoformat()
        }

    def get_location_fallback(user_id, **kwargs):
        """Fallback : géolocalisation approximative"""
        return {
            "user_id": user_id,
            "latitude": 48.8566,  # Paris par défaut
            "longitude": 2.3522,
            "accuracy": "low",
            "source": "fallback",
            "timestamp": datetime.now().isoformat()
        }

    # Tests de dégradation
    print("\n   1️⃣ Tests de dégradation progressive :")

    for i in range(10):
        try:
            location = geo_service.call_with_fallback(
                get_location_full,
                get_location_fallback,
                user_id=f"user_{i+1}"
            )
            print(
                f"   📍 Appel {i+1}: {location['accuracy']} accuracy - {location.get('source', 'primary')}")

        except Exception as e:
            print(f"   💥 Appel {i+1}: Échec total - {e}")

        time.sleep(0.1)

    # État final du service
    print(f"\n   📊 État final du service:")
    print(f"      Niveau: {geo_service.level}")
    print(f"      Erreurs: {geo_service.error_count}")
    print(
        f"      Cache disponible: {'last_result' in geo_service.fallback_data}")


demo_graceful_degradation()

print("\n" + "=" * 50)
print("6. MONITORING ET ALERTES")
print("=" * 50)

print("\n📈 SYSTÈME DE MONITORING D'ERREURS")
print("-" * 35)


class ErrorMonitor:
    """Système de monitoring et d'alertes pour erreurs"""

    def __init__(self):
        self.metrics = {
            "error_rate": [],
            "response_times": [],
            "error_types": {},
            "alerts_sent": 0
        }
        self.alert_thresholds = {
            "error_rate": 0.1,      # 10% d'erreurs
            "avg_response_time": 5.0,  # 5 secondes
            "error_spike": 5         # 5 erreurs en 1 minute
        }
        self.alert_cooldown = 60  # 1 minute entre alertes
        self.last_alert_time = 0

    def record_request(self, success: bool, response_time: float, error_type: str = None):
        """Enregistrer une requête"""
        timestamp = time.time()

        # Métriques de base
        self.metrics["error_rate"].append({
            "timestamp": timestamp,
            "success": success
        })

        self.metrics["response_times"].append({
            "timestamp": timestamp,
            "duration": response_time
        })

        # Types d'erreurs
        if not success and error_type:
            self.metrics["error_types"][error_type] = \
                self.metrics["error_types"].get(error_type, 0) + 1

        # Nettoyer les vieilles données (garde 5 minutes)
        cutoff = timestamp - 300
        self.metrics["error_rate"] = [
            m for m in self.metrics["error_rate"]
            if m["timestamp"] > cutoff
        ]
        self.metrics["response_times"] = [
            m for m in self.metrics["response_times"]
            if m["timestamp"] > cutoff
        ]

        # Vérifier les alertes
        self._check_alerts()

    def _check_alerts(self):
        """Vérifier si des alertes doivent être envoyées"""
        now = time.time()

        # Cooldown des alertes
        if now - self.last_alert_time < self.alert_cooldown:
            return

        alerts = []

        # Taux d'erreur
        if len(self.metrics["error_rate"]) >= 10:  # Minimum 10 requêtes
            errors = sum(
                1 for m in self.metrics["error_rate"] if not m["success"])
            error_rate = errors / len(self.metrics["error_rate"])

            if error_rate > self.alert_thresholds["error_rate"]:
                alerts.append(f"Taux d'erreur élevé: {error_rate:.1%}")

        # Temps de réponse moyen
        if len(self.metrics["response_times"]) >= 10:
            avg_time = sum(m["duration"] for m in self.metrics["response_times"]
                           ) / len(self.metrics["response_times"])

            if avg_time > self.alert_thresholds["avg_response_time"]:
                alerts.append(f"Temps de réponse lent: {avg_time:.2f}s")

        # Pic d'erreurs
        recent_errors = sum(
            1 for m in self.metrics["error_rate"]
            if not m["success"] and now - m["timestamp"] < 60
        )

        if recent_errors >= self.alert_thresholds["error_spike"]:
            alerts.append(f"Pic d'erreurs: {recent_errors} en 1 minute")

        # Envoyer les alertes
        if alerts:
            self._send_alert(alerts)

    def _send_alert(self, alerts: List[str]):
        """Envoyer une alerte"""
        self.last_alert_time = time.time()
        self.metrics["alerts_sent"] += 1

        print(f"   🚨 ALERTE #{self.metrics['alerts_sent']} :")
        for alert in alerts:
            print(f"      • {alert}")
        print(f"      Timestamp: {datetime.now().strftime('%H:%M:%S')}")

    def get_dashboard(self) -> str:
        """Générer un dashboard de monitoring"""
        now = time.time()

        # Calculs des métriques
        total_requests = len(self.metrics["error_rate"])
        if total_requests == 0:
            return "Aucune donnée disponible"

        successful = sum(1 for m in self.metrics["error_rate"] if m["success"])
        error_rate = (total_requests - successful) / total_requests

        avg_response_time = 0
        if self.metrics["response_times"]:
            avg_response_time = sum(
                m["duration"] for m in self.metrics["response_times"]) / len(self.metrics["response_times"])

        # Top erreurs
        top_errors = sorted(self.metrics["error_types"].items(
        ), key=lambda x: x[1], reverse=True)[:3]

        dashboard = [
            "=" * 40,
            "📊 DASHBOARD DE MONITORING",
            "=" * 40,
            f"⏱️  Période: dernières {len(self.metrics['error_rate'])} requêtes",
            f"✅ Taux de succès: {(1-error_rate):.1%}",
            f"❌ Taux d'erreur: {error_rate:.1%}",
            f"⚡ Temps de réponse moyen: {avg_response_time:.2f}s",
            f"🚨 Alertes envoyées: {self.metrics['alerts_sent']}",
            "",
            "🔝 TOP ERREURS:"
        ]

        for error_type, count in top_errors:
            dashboard.append(f"   • {error_type}: {count}")

        if not top_errors:
            dashboard.append("   Aucune erreur récente")

        return "\n".join(dashboard)


def demo_error_monitoring():
    """Démonstration du monitoring d'erreurs"""

    print("📈 Système de monitoring d'erreurs :")

    monitor = ErrorMonitor()

    # Simuler des requêtes avec différents patterns
    def simulate_requests():
        """Simuler des requêtes avec différents profils"""
        import random

        scenarios = [
            # Phase normale
            {"success_rate": 0.95, "avg_time": 1.0,
                "requests": 20, "name": "Normal"},
            # Dégradation
            {"success_rate": 0.8, "avg_time": 3.0,
                "requests": 15, "name": "Dégradé"},
            # Incident
            {"success_rate": 0.5, "avg_time": 8.0,
                "requests": 10, "name": "Incident"},
            # Récupération
            {"success_rate": 0.9, "avg_time": 2.0,
                "requests": 15, "name": "Récupération"},
        ]

        error_types = ["TimeoutError", "ConnectionError",
                       "ValueError", "RuntimeError"]

        for scenario in scenarios:
            print(f"\n   📋 Phase: {scenario['name']}")

            for i in range(scenario["requests"]):
                # Déterminer si succès ou échec
                success = random.random() < scenario["success_rate"]

                # Temps de réponse
                base_time = scenario["avg_time"]
                response_time = max(0.1, random.gauss(
                    base_time, base_time * 0.3))

                # Type d'erreur si échec
                error_type = None if success else random.choice(error_types)

                # Enregistrer la requête
                monitor.record_request(success, response_time, error_type)

                # Affichage occasionnel
                if i % 5 == 0:
                    status = "✅" if success else "❌"
                    print(
                        f"      Requête {i+1}: {status} {response_time:.2f}s")

                time.sleep(0.05)  # Petite pause

    # Lancer la simulation
    print("\n   🎬 Simulation de trafic avec monitoring :")
    simulate_requests()

    # Afficher le dashboard final
    print("\n   📊 Dashboard final :")
    dashboard = monitor.get_dashboard()
    print(dashboard)


demo_error_monitoring()

print("\n" + "=" * 50)
print("7. EXERCICES PRATIQUES")
print("=" * 50)

print("""
💪 EXERCICES À IMPLÉMENTER :

🎯 Exercice 1 : Système de Health Check
Créez un système de surveillance de santé :
• Health checks pour services externes
• Agrégation de statuts avec poids
• Dashboard temps réel
• Alertes configurables par seuil
• Historique et tendances

🔧 Exercice 2 : Framework de Retry Intelligent
Créez un système de retry avancé :
• Stratégies multiples (linear, exponential, fibonacci)
• Retry basé sur type d'exception
• Jitter pour éviter thundering herd
• Circuit breaker intégré
• Métriques et observabilité

🎮 Exercice 3 : Error Recovery System
Créez un système de récupération automatique :
• Détection de patterns d'erreurs
• Actions correctives automatiques
• Escalation vers humains
• Machine learning pour prédiction
• Self-healing capabilities

⚡ Exercice 4 : Distributed Error Tracking
Créez un système de tracking distribué :
• Corrélation d'erreurs entre services
• Trace IDs et spans
• Causality tracking
• Impact analysis
• Root cause analysis automatique

🌐 Exercice 5 : Chaos Engineering Framework
Créez un framework de chaos engineering :
• Injection d'erreurs contrôlée
• Simulation de pannes réseau
• Test de résilience automatisé
• Metrics de récupération
• Game days orchestrés
""")

print("\n" + "=" * 50)
print("8. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. 🔗 EXCEPTION CHAINING AVANCÉ :
   • Exception context avec from pour debugging
   • Custom exception hierarchies pour métier
   • Préservation du stack trace original
   • Enrichissement avec contexte business

2. 🎨 DÉCORATEURS POUR ERROR HANDLING :
   • @retry avec backoff configurable
   • @handle_exceptions pour gestion automatique
   • @validate_args pour validation précoce
   • Composition de décorateurs pour robustesse

3. ⚡ CIRCUIT BREAKER PATTERN :
   • États CLOSED/OPEN/HALF_OPEN
   • Métriques et seuils configurables
   • Recovery automatique et test
   • Protection contre cascades de pannes

4. 📊 ERROR AGGREGATION :
   • Collecte centralisée des erreurs
   • Métriques temps réel et historiques
   • Alertes basées sur seuils
   • Reporting et dashboards

5. 🛡️ GRACEFUL DEGRADATION :
   • Niveaux de service dégradés
   • Fallbacks et données en cache
   • Recovery automatique
   • Préservation de l'expérience utilisateur

💡 PATTERNS AVANCÉS :
✅ Exception chaining pour contexte complet
✅ Décorateurs composables pour error handling
✅ Circuit breakers pour résilience
✅ Monitoring proactif avec alertes
✅ Dégradation gracieuse des services
✅ Recovery automatique et self-healing

🚨 ANTI-PATTERNS À ÉVITER :
❌ Exceptions génériques sans contexte
❌ Retry sans backoff (thundering herd)
❌ Masquage d'erreurs importantes
❌ Pas de monitoring des erreurs
❌ Failure sans fallback
❌ Recovery sans validation

⚡ ARCHITECTURE RÉSILIENTE :
• Séparation des préoccupations d'erreur
• Observabilité et métriques complètes
• Fault isolation et containment
• Auto-scaling basé sur health
• Graceful shutdown et startup

🔧 OUTILS ET FRAMEWORKS :
• APM (Application Performance Monitoring)
• Distributed tracing (Jaeger, Zipkin)
• Circuit breakers (Hystrix, Resilience4j)
• Chaos engineering (Chaos Monkey)
• Error tracking (Sentry, Rollbar)

🎯 STRATÉGIES DE PRODUCTION :
• Error budgets et SLOs
• Incident response automatisé
• Postmortem et learning culture
• Chaos engineering régulier
• Continuous resilience testing

🔍 OBSERVABILITÉ :
• Métriques d'erreurs en temps réel
• Logs structurés avec corrélation
• Traces distribuées pour debugging
• Alertes proactives et smart
• Dashboards pour visibility

🎉 Félicitations ! Error handling avancé maîtrisé !
💡 Prochaine étape : Programmation orientée objet !
📚 Erreurs sous contrôle, programmez en OOP !
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - TRY/CATCH AVANCÉ MAÎTRISÉ !")
print("=" * 70)
