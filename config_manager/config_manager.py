#!/usr/bin/env python2

"""
This module takes care of loading a default and custom config
and providing the final set of config.

Custom config >> default config

Sample problem and output:
==========================


P <-- default config
Q <-- custom config

Input:

P = {
   x: {
      a: 1
      b: 2
      c: 3
      }
   y: 7
   u: 4
   }


Q = {
   x: {
      b: 6
      d: 8
      }
   y: 5
   z: 9
   }


Q->P = {
   x: {
      a: 1
      b: 6
      c: 3
      d: 8
      }
   y: 5
   u: 4
   z: 9
   }

"""

from copy import deepcopy


class ConfigManager(object):
    """
    Manages configs with precedence
    Given a default and custom config, merges two configs together
    with common configs merged together with a precendence for custom
    configs' matching keys and their values
    """

    def common_keys(self, a, b):
        """
        Returns common keys between given two dictionaries
        """
        return list(set(a.keys()) & set(b.keys()))

    def a_minus_b(self, a, b):
        """
        Given two list a and b, this method returns exclusive
        elements of list a which are absent in list b
        """
        return list(set(a) - set(b))

    def iterative_config_map(self, default, custom):
        """
        Takes care of mapping iterative configs
        """
        final_config = {}
        # lets find out common keys to be manage
        common_keys = self.common_keys(default, custom)

        # configs of the custom takes precedence over default config
        for key in common_keys:
            if isinstance(custom[key], int):
                final_config[key] = custom[key]
            else:
                final_config[key] = self.iterative_config_map(
                    default[key],
                    custom[key])

        # lets add default config keys not available in custom config
        exclusive_keys_of_default_config = self.a_minus_b(
                default.keys(), common_keys)

        for key in exclusive_keys_of_default_config:
            # deepcopy copies over the nested dictionaries as well
            # by creating new references
            final_config[key] = deepcopy(default[key])

        # lets add newly added keys in custom config to final config
        exclusive_keys_of_custom_config = self.a_minus_b(
                custom.keys(), common_keys)

        for key in exclusive_keys_of_custom_config:
            final_config[key] = deepcopy(custom[key])

        return final_config


if __name__ == "__main__":

    P = {
        'x': {
            'a': 1,
            'b': 2,
            'c': 3,
        },
        'y': 7,
        'u': 4,
    }
    Q = {
        'x': {
            'b': 6,
            'd': 8,
        },
        'y': 5,
        'z': 9,
    }

    cc = ConfigManager()
    print (cc.iterative_config_map(P, Q))
